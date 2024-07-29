import datetime

from django.db import models
from enum import Enum

from file_upload.models import UploadedFile
from model_app.abstract_base.models import BaseModel, BaseModelLite
from model_app.waste.models import WasteSite
from notification.models import Notice
from workflow.decorators import operation
from notification import constants as c


class StatusesOfCompletions(Enum):
    ERROR = "Интеграция не завершена. Ошибка."
    SUCCESS = "Интеграция успешно завершена."


class AsuOdsExport(models.Model):
    request_raw = models.TextField('Сырой запрос экспорта', null=True, blank=True)
    request_error = models.TextField('Ошибка запроса экспорта', null=True, blank=True)
    request_id = models.CharField('ID запроса', max_length=255, null=True, blank=True)
    response_raw = models.TextField('Сырой ответ экспорта', null=True, blank=True)
    response_error = models.TextField('Ошибка ответ экспорта', null=True, blank=True)
    response_url = models.TextField('URL с файлом выгрузки', null=True, blank=True)
    parse_error = models.TextField('Ошибка парсинга экспорта', null=True, blank=True)
    datetime_create = models.DateTimeField('Время добавления', auto_now_add=True)
    datetime_update = models.DateTimeField('Время обновления', auto_now=True)
    result_file = models.OneToOneField(UploadedFile, on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name="Файл с данными ответа")
    log = models.TextField("История", blank=True)
    command_name = models.CharField(max_length=300, default="", blank=True)
    status_of_completion = models.CharField("Статус завершения", max_length=7, default="", blank=True,
                                            choices=[(s.name, s.value) for s in StatusesOfCompletions])

    class Meta:
        verbose_name = 'АСУ ОДС экспорт'
        verbose_name_plural = 'АСУ ОДС экспорты'

    def __str__(self):
        return str(self.request_id)


class AsuOdsTransport(BaseModel):
    number = models.TextField('Госномер', null=True, blank=True)
    place = models.TextField('Местонажождение', null=True, blank=True)
    transporter = models.TextField('Перевозчик', null=True, blank=True)
    brand = models.TextField('Марка', null=True, blank=True)
    type = models.TextField('Тип', null=True, blank=True)
    base = models.TextField('База', null=True, blank=True)
    park = models.TextField('Автопарк', null=True, blank=True)
    operator = models.TextField('Оператор', null=True, blank=True)
    model = models.TextField('Модель', null=True, blank=True)
    number_garage = models.TextField('Гаражный номер', null=True, blank=True)
    vin = models.TextField('VIN - номер', null=True, blank=True)
    tracker_id = models.TextField('Трекер - id', null=True, blank=True)
    date_sync = models.DateTimeField('Дата синхронизации', null=True, blank=True)
    is_special = models.BooleanField('Специализированное транспортное средство', default=False)
    hazard_class = models.TextField('Класс опасности', null=True, blank=True)
    capacity = models.TextField('Вместимость', null=True, blank=True)
    weight = models.TextField('Грузоподъемность', null=True, blank=True)

    @operation(title='Обновить из АСУ ОДС', operation_type='all',
               access_rules_from='get', icon='uicon uicon-xls-export')
    def update_transport(self, request, **kwargs):
        Notice.send_notice(
            request.user,
            operation_type=c.OPERATION_INFO,
            content=f"Запущено обновление транспорта из АСУ ОДС ПСД",
            theme=c.THEME_SHOW
        )
        AsuOdsTransport.objects.all().update(date_sync=datetime.datetime.now(tz=datetime.timezone.utc))

        Notice.send_notice(
            request.user,
            operation_type=c.OPERATION_INFO,
            content=f"Обновление транспорта из АСУ ОДС ПСД завершено",
            theme=c.THEME_SUCCESS
        )
        return [], 200

    class Meta:
        verbose_name = 'АСУ ОДС Транспорт'
        verbose_name_plural = 'АСУ ОДС Транспорт'


class WasteSiteRawData(BaseModelLite):
    """Хранит сырые данные об МНО полученные из АСУ ОДС"""

    lon = models.DecimalField(  # Для мно обозначенных полигонами вычисляется средняя точка.
        max_digits=9, decimal_places=6, blank=True, null=True, db_index=True, verbose_name='Долгота'
    )
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True, db_index=True, verbose_name='Широта'
    )
    raw_data = models.JSONField()
    object_id = models.IntegerField(unique=True, db_index=True)
    nearest_mno = models.ForeignKey(WasteSite, on_delete=models.SET_NULL, null=True,
                                    blank=True, related_name='+', verbose_name="Ближайшее МНО")

    class Meta:
        verbose_name = 'Сырые данные по МНО'
        verbose_name_plural = 'Список сырых данных по МНО'

    def has_coords(self) -> "bool":
        return bool(self.lat and self.lon)

    def has_equal_raw_data(self, raw_waste_site: "WasteSiteRawData") -> "bool":
        return self.raw_data == raw_waste_site.raw_data

    def update_obj_data(self, obj: "WasteSiteRawData"):
        """Обновляет свои данные из ещё не сохранённого объекта, который создавался из полученных данных"""
        if self.object_id != obj.object_id:
            raise ValueError("Ошибка. Попытка обновить данные одной МНО из данных совершенно другой: "
                             f" {self.object_id} <- {obj.object_id}")
        self.lon = obj.lon
        self.lat = obj.lat
        self.raw_data = obj.raw_data

