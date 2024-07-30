import datetime
import json
import os
import time
from typing import List

import pytz
import requests
import zipfile

from dateutil.relativedelta import relativedelta
from django.core.management import BaseCommand

from asu_ods_integration.exceptions import RequestError
from asu_ods_integration.import_containers import ImportContainerManager
from asu_ods_integration.models import AsuOdsExport, StatusesOfCompletions
from asu_ods_integration.external.asu_ods import AsuOds
from data_exchange_with_external_systems.logging_of_tasks import LogManager


class Command(BaseCommand):
    _mno_raw_data: "List" = None
    _export_obj: "AsuOdsExport" = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._log_manager = LogManager("ods_integration")
        self._import_mno_manager = self._create_import_manager()

    def _create_import_manager(self) -> "ImportContainerManager":
        return ImportContainerManager(self._log_manager)

    @property
    def command_name(self):
        s = os.path.basename(__file__).split(".")[0]
        return s

    def add_arguments(self, parser):
        parser.add_argument("start_date", default=None, nargs="?", type=str)
        parser.add_argument("end_date", default=None, nargs="?", type=str)
        parser.add_argument("--number_of_month", default=None, type=int)

    def handle(self, start_date=None, end_date=None, number_of_month=None, **options):
        s = time.time()
        try:
            self._log_manager.log.info(f"Была вызвана команда <{self.command_name}>.")
            start_date_str = start_date
            end_date_str = end_date
            start_date, end_date = self.get_start_date_and_end_date(start_date_str, end_date_str, number_of_month)
            start_dt, end_dt = self.convert_dates_to_datetimes(start_date, end_date)

            try:
                self._export_obj = self.request(start_dt, end_dt)
                self._export_obj.command_name = self.command_name
                self._log_manager.set_obj(self._export_obj)
            except (requests.exceptions.ConnectionError, RequestError) as e:
                print("Выполняется нужный код")
                self._export_obj = AsuOds.create_empty_export_obj(self.command_name, StatusesOfCompletions.ERROR)
                self._log_manager.set_obj(self._export_obj)
                self._log_manager.log.error(f"Ошибка подключения к серверу: {repr(e)}.\nРабота программы завершена.")
                # self._log_manager.finish()
                print("Выполнение завершено")
                raise e

            # Ожидание ответа от ОДС
            timer = 0
            for _ in range(50):
                self._log_manager.save_log()
                self._log_manager.log.info(f"Ожидание обратного запроса от АСУ ОДС")
                time.sleep(5)
                timer += 5
                self._log_manager.log.info(f"Длительность ожидания {timer} секунд.")
                if not self.has_request_from_ods():
                    continue
                else:
                    self._log_manager.log.info("АСУ ОДС прислал запрашиваемые данные.")
                    break
            else:
                self._log_manager.log.warning("Время ожидания истекло. Нужно увеличить время ожидания"
                                              " или попробовать ещё один запрос.")
                self._log_manager.log.info("Работа программы завершена.")
                self._log_manager.save_log()
                return  # Завершение работы команды, так-как данных не поступило.

            self._mno_raw_data = self.download_file(self._export_obj)

            # Код для использования на локальной машине
            # from django.conf import settings
            # import json
            # path_to_file = os.path.join(settings.BASE_DIR, "mno.json")
            # print("Путь к файлу", path_to_file)
            # with open(path_to_file, "r") as file:
            #     area_data = []
            #     for line in file.readlines():
            #         j_line = json.loads(line)
            #         area_data.append(j_line)
            #     self._mno_raw_data = area_data

            self._import_mno_manager.import_raw_data(self._mno_raw_data)
            e = time.time() - s
            self._log_manager.log.info(f"Все расчёты были выполнены за {e}")
            self._log_manager.save_log()
            self._export_obj.status_of_completion = StatusesOfCompletions.SUCCESS.name
            self._export_obj.save()
        except Exception as e:
            self._log_manager.log.error("", exc_info=True)
            if self._export_obj:
                self._log_manager.save_log()
                self._export_obj.status_of_completion = StatusesOfCompletions.ERROR.name
                self._export_obj.save()
            raise e
        finally:
            self._log_manager.close_io()

    def request(self, start_dt: "datetime.datetime", end_dt: "datetime.datetime") -> "AsuOdsExport":
        export_obj = AsuOds.request_ogh('container', start_dt, end_dt)
        return export_obj

    def create_datetime_range_of_month(self, number_of_month):
        try:
            number_of_month = int(number_of_month)
        except ValueError:
            raise ValueError("Ошибка. Ключ --number_of_mont должен быть целым числом.")
        if not isinstance(number_of_month, int) or 12 < number_of_month <= 0:
            raise ValueError("Неверное значение number_of_month. Должно быть целое 1-12")
        date = datetime.date.today()
        start_dt = datetime.datetime(year=date.year, month=number_of_month, day=1, tzinfo=datetime.timezone.utc)
        end_dt = start_dt + relativedelta(months=1)
        return start_dt, end_dt

    def create_today_date_range(self):
        """
        Используется, если не была определена ни одна из переменных.
        Тогда запрашиваются данные за последние сутки.
        """
        today_dt = datetime.datetime.utcnow()
        today_dt: "datetime.datetime" = pytz.utc.localize(today_dt)
        start_date = today_dt.date()
        end_date = today_dt.date()
        return start_date, end_date

    def parse_date_str(self, date_str):
        try:
            if "T" in date_str:
                d = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
            else:
                d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверно указана дата {date_str}. Формат даты должен быть: гггг-мм-дд")
        return d

    def get_start_date_and_end_date(self, start_date_str, end_date_str, number_of_month):
        if (start_date_str or end_date_str) and not (start_date_str and end_date_str):
            # была указана только одна переменная из двух
            raise ValueError("При указании диапазона дат, нужно указывать обе даты: start_date, end_date, или не одной")
        elif start_date_str and end_date_str and number_of_month:
            raise ValueError("Указаны все три аргумента. Что вы хотели, данные за период или данные за месяц?"
                             "Подсказка: указывайте или период или номер месяца")
        elif start_date_str and end_date_str:
            start_date = self.parse_date_str(start_date_str)
            end_date = self.parse_date_str(end_date_str)
            if end_date < start_date:
                raise ValueError("Ошибка: конечная дата меньше чем начальная.")
        elif number_of_month:
            start_date, end_date = self.create_datetime_range_of_month(number_of_month)
        else:
            raise RuntimeError()
        return start_date, end_date

    def convert_dates_to_datetimes(self, start_date: "datetime.datetime", end_date: "datetime.datetime"):
        start_dt = start_date.combine(start_date, datetime.time(hour=0))
        end_dt = end_date.combine(end_date, datetime.time(hour=23, minute=59, second=59))
        return start_dt, end_dt

    def download_file(self, export_obj: "AsuOdsExport"):
        path_to_management = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_temporary_files = os.path.join(path_to_management, "temporary_files")
        response_json = json.loads(export_obj.response_raw)
        link = response_json["url"]

        if not os.path.exists(path_to_temporary_files):
            os.mkdir(path_to_temporary_files)
        response = requests.get(
            link, timeout=60,
        )

        file_path_to_zip_file = os.path.join(path_to_temporary_files, "temporary_file.zip")

        with open(file_path_to_zip_file, "wb") as f_zip:
            f_zip.write(response.content)

        with zipfile.ZipFile(file_path_to_zip_file, "r") as f_zip:
            f_zip.extractall(path_to_temporary_files)
            unzip_file_name = f_zip.namelist()[0]  # Присылают всегда только один файл

        file_path_to_unzip_file = os.path.join(path_to_temporary_files, unzip_file_name)

        with open(file_path_to_unzip_file, "r") as f_unzip:
            area_data = []
            for line in f_unzip.readlines():
                j_line = json.loads(line)
                area_data.append(j_line)

        # shutil.rmtree(path_to_temporary_files)  # проще удалить всю папку, чтобы удалить временные файлы
        return area_data

    def has_request_from_ods(self):
        self._export_obj.refresh_from_db()
        b = self._export_obj.response_raw
        return b
