"""
Одноразовый код для поиска импортированных вручную площадок.
Ожидает выполнения.
"""

import csv
import time

from django.core.management import BaseCommand
from django.db.models import Q
from typing import Optional

from functools import lru_cache

from data_exchange_with_external_systems import constants
from asu_ods_integration.import_containers import WasteSiteFinderTemp
from asu_ods_integration.utilites import GeoPoint
from model_app.base.models import Participant
from model_app.waste import WASTE_SITE_CATEGORIES
from model_app.waste.models import WasteSite

FILE_NAME = 'mno_asu_ods.csv' # файл удален из гита  - помещен в облако platform_files/mno_asu_ods.csv

class Command(BaseCommand):
    _waste_sites_updated = []
    _waste_sites_30m_updated = []
    _excluded_from_update = []
    _participant_dict = {}

    def handle(self, **options):
        print("Выполняется поиск площадок.")
        start = time.time()

        def round_float(n):
            """Округляет вниз, до пятого знака после запятой"""
            n = int(n * 100_000) / 100_000
            return n

        # Поиск тех МНО среди которых нужно искать созданные вручную.
        ws_list = list(WasteSite.objects.filter(lat__isnull=False, lon__isnull=False))
        print("На сервере площадок с координатами", len(ws_list))

        with open(FILE_NAME, newline='\n', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=";")
            all_mno_ods_data = list(reader)[1:]

        print("Вычисляются совпадения")
        waste_site_finder = WasteSiteFinderTemp()
        updated = set()
        for i, ods_mno in enumerate(all_mno_ods_data):
            if not (i % 1000):
                print("Обработано площадок", i)
            ods_id = ods_mno[0].strip()
            ods_lat = float(ods_mno[1])
            ods_lon = float(ods_mno[2])
            participant_name = ods_mno[3]  # Балансодержатель

            ods_lat_round = round(ods_lat, 5)
            ods_lon_round = round(ods_lon, 5)

            ods_lat_floor = round_float(ods_lat)
            ods_lon_floor = round_float(ods_lon)

            waste_sites_for_update_qs = WasteSite.objects.filter(
                Q(lat=ods_lat, lon=ods_lon) |
                Q(lat=ods_lat_round, lon=ods_lon_round) |
                Q(lat=ods_lat_floor, lon=ods_lon_floor)
            )
            participant = self.get_participant_by_name(participant_name)
            for ws in waste_sites_for_update_qs:
                self.update_waste_site(ws, ods_id, participant)
                self._waste_sites_updated.append(ods_id)
                updated.add(ods_id)

        for i, ods_mno in enumerate(all_mno_ods_data):
            ods_id = ods_mno[0].strip()
            ods_lat = float(ods_mno[1])
            ods_lon = float(ods_mno[2])
            participant_name = ods_mno[3]  # Балансодержатель
            category = ods_mno[4]  # Категория

            if ods_id in updated:
                continue

            if not (i % 1000):
                print("Обработано площадок", i)

            point = GeoPoint(ods_lat, ods_lon)
            waste_site_finder.set_point_for_analyze(point)
            waste_sites = waste_site_finder.find_nearby_locations(30)
            waste_sites = list(waste_sites)
            if waste_sites:
                print("В радиусе 30 метров были найдены площадки", waste_sites)
                # print("Имя контрагента", participant_name)
            for ws in waste_sites:
                if ws.ext_id and ws.ext_id == str(ods_id):
                    # print("Причина обновления внешний ключ")
                    participant = self.get_participant_by_name(participant_name)
                    self.update_waste_site(ws, ods_id, participant, category=category)
                    self._waste_sites_30m_updated.append(ws)
                elif ws.participant and participant_name and \
                        ws.participant.name.lower().strip() == participant_name.lower().strip():
                    # print("Причина обновления имя контрагента")
                    self.update_waste_site(ws, ods_id, ws.participant, category=category)
                    self._waste_sites_30m_updated.append(ws)
                else:
                    continue

        print("Всего успешных обновлений", len(self._waste_sites_updated))
        print("Обновлённые площадки", [ws_id for ws_id in self._waste_sites_updated])
        print("Найденных площадок в радиусе 30 метров и обновлённых", len(self._waste_sites_30m_updated))
        print("Список обновлённых, по радиусу, площадок:", [w.id for w in self._waste_sites_30m_updated])
        print("Площадки, которые нужно обновлять, но все их поля уже имеют требуемые значения",
              len(self._excluded_from_update), self._excluded_from_update)
        end = time.time() - start
        print("Выполнение команды завершено. Время выполнения", end)

    def update_waste_site(self, waste_site: "WasteSite", ext_id: "str",
                          participant: "Participant" = None, category: "str" = None):
        category_number = self.get_category_number(category)

        # Нужно ли обновлять площадку
        if (waste_site.ext_id != ext_id or
                waste_site.external_source != constants.ExternalSources.ODS.name or
                (participant and waste_site.participant != participant) or
                (category_number and waste_site.category != category_number)):
            # Само обновление
            waste_site.ext_id = ext_id
            waste_site.external_source = constants.ExternalSources.ODS.name
            if participant:
                waste_site.participant = participant
            if category:
                waste_site.category = category_number
            waste_site.save()
            self._waste_sites_updated.append(waste_site)
            print("Была обновлена площадка", waste_site)
        else:
            # print("Площадка была исключена из обновления", waste_site)
            self._excluded_from_update.append(waste_site)

    @lru_cache(maxsize=20)
    def get_category_number(self, category_name: str) -> "Optional[int]":
        if category_name:
            for value, name in WASTE_SITE_CATEGORIES:
                if category_name.lower().strip() == name.lower().strip():
                    v = value
                    break
            else:
                v = None
        else:
            v = None
        print("Было возвращено", v)
        return v

    def get_participant_by_name(self, participant_name: "str") -> "Optional[Participant]":
        participant_name = participant_name.strip()
        try:
            participant = self._participant_dict[participant_name]
        except KeyError:
            try:
                participant = Participant.objects \
                    .filter(name__iexact=participant_name.strip()) \
                    .earliest("datetime_create")
                self._participant_dict[participant_name] = participant
                print("Был найден новый")
            except Participant.DoesNotExist:
                participant = None
                self._participant_dict[participant_name] = participant
        # print("Возвращается", participant, "Функция выполнялась", round(time.time() - start, 3))
        return participant

