import datetime
import logging
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from typing import List, Any, Optional

from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from eav.models import Attribute, Value
from data_exchange_with_external_systems.logging_of_tasks import LogManager
from workflow.models import DocType, DocItem, DocStatus

PrepareCell = namedtuple('PrepareCell', ['name', 'code', 'value'])


class EAVCreator(metaclass=ABCMeta):
    """
    Планировалась логика, которая бы принимала любые данные на определённую тематику,
    и создавала по ним EAV-сущность и данные к ней.
    """
    _doc_type: "DocType" = None

    def __init__(self, doctype_name: "Optional[str]", doctype_code: "str",
                 raw_data: "List[dict]", log_manager: "LogManager"):
        """
        doctype_code - используется для поиска нужного DocType, если же он не найден, то создаётся
        новый по имени и коду.
        """
        self._log_manager = log_manager
        self._doctype_name = doctype_name
        self._doctype_code = doctype_code
        self._raw_data = raw_data
        self._attributes = {}
        self._data_example = None  # Пример данных по которым соберётся DocType или Attribute к нему.

    @transaction.atomic
    def create_eav(self):
        """Главный метод. Можно переопределить, чтобы изменить порядок алгоритма, для своей задачи."""
        if not self._data_example:
            raise ValueError("Не задан атрибут self._data_example.")
        prepared_documents = self._prepare_data(self._raw_data)
        self._get_or_create_doctype()
        self._data_example = prepared_documents[0]
        field_names_and_codes = [PrepareCell(name=k, code=k, value=v) for k, v in self._data_example.items()]
        self._log_manager.log.info("Создаются атрибуты")
        self._log_manager.save_log()
        self._create_attributes(field_names_and_codes)
        self._doc_type.attributes.add(*self._attributes.values())

        # Сборка данных
        self._log_manager.log.info("Создаются документы")
        self._log_manager.save_log()
        self._load_documents(prepared_documents)

    def set_data_example(self, example_data: "dict"):
        """
        Устанавливает данные, по анализу которых добавятся аттрибуты, в DocType.
        Ожидается одноуровневый словарь.
        """
        self._data_example = example_data

    def _get_or_create_doctype(self):
        try:
            self._doc_type = DocType.objects.get(
                code=self._doctype_code,
            )
        except DocType.DoesNotExist:
            self._doc_type = DocType.objects.create(
                name=self._doctype_name,
                name_plural=self._doctype_name,
                code=self._doctype_code,
                is_active=False,
                table=ContentType.objects.get_for_model(DocItem),
            )

    def _create_attributes(self, attributes_names: "List[PrepareCell]"):
        """Создаёт атрибуты, по переданным в метод данным"""
        for prepared_cell in attributes_names:
            slug = self.get_slug(prepared_cell.code)
            try:
                a = Attribute.objects.get(slug=slug)
            except Attribute.DoesNotExist:
                a = Attribute.objects.create(
                    name=prepared_cell.name,
                    slug=slug,
                    datatype=self._get_datatype(prepared_cell.value),
                    required=False,
                    description=None,
                )
            self._attributes[slug] = a

    def get_slug(self, field_code: "str"):
        s = self._doc_type.code + "__" + field_code
        return s

    def _get_datatype(self, value: "Any"):
        """Метод должен определять тип данных атрибута (колонки)"""
        if isinstance(value, str):
            t = Attribute.TYPE_TEXT
        elif isinstance(value, bool):
            t = Attribute.TYPE_BOOLEAN
        elif isinstance(value, int):
            t = Attribute.TYPE_INT
        elif isinstance(value, float):
            t = Attribute.TYPE_FLOAT
        elif isinstance(value, datetime.datetime):
            t = Attribute.TYPE_DATE_TIME
        elif isinstance(value, datetime.date):
            t = Attribute.TYPE_DATE
        else:
            t = Attribute.TYPE_TEXT
        return t

    def _load_documents(self, all_data: "list"):
        """Создаёт необходимое количество DocItem, в соответствии с присланными данными."""
        doc_status = DocStatus.objects.latest("id")
        for i, data in enumerate(all_data):
            with transaction.atomic():
                doc_item = DocItem.objects.create(
                    number=i,
                    doc_type=self._doc_type,
                    is_active=False,
                    status=doc_status,
                )
                for k, v in data.items():
                    attr = self._attributes[self.get_slug(k)]
                    value = Value(
                        attribute=attr,
                        entity=doc_item,
                    )
                    value.value = str(v)
                    value.save()
            self._log_manager.log.info(f"Создан документ {i + 1}, из {len(all_data)}")
            self._log_manager.save_log()

    @abstractmethod
    def _prepare_data(self, raw_data) -> "List[dict]":
        """
        Двухуровневые словари с данными, переводятся в одноуровневые с объединением ключей, на примере
        интеграции с АСУ ОДС
        Хотя, наверно, можно использовать тип "объект" для создания дерева.
        """
        pass


class AsuOdsEavCreator(EAVCreator):

    def _prepare_data(self, raw_data) -> "List[dict]":
        log = logging.getLogger("ods_integration")
        log.info("Начался этап подготовки данных")
        prepared_data = []
        for d in raw_data:
            document_data = {}
            for k, v in d.items():
                if isinstance(v, dict):
                    for k2, v2 in v.items():
                        field_name = str(k) + "__" + str(k2)
                        value = v2
                        document_data[field_name] = value
                elif isinstance(v, list):
                    # Списки пропускаются
                    continue
                else:
                    field_name = str(k)
                    value = v
                    document_data[field_name] = value
            prepared_data.append(document_data)
        return prepared_data
