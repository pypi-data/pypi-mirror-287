import logging
import statistics
import time
from abc import ABCMeta, abstractmethod
from functools import lru_cache
from typing import List, Optional, Union, Tuple, Dict

import datetime
import pyproj
from dataclasses import dataclass

from django.contrib.auth.models import User
from django.contrib.gis import geos

from asu_ods_integration import utilites
from asu_ods_integration.models import WasteSiteRawData
from asu_ods_integration.utilites import GeoPoint, AbstractNearestLocationFinder
from data_exchange_with_external_systems.constants import ExternalSources
from data_exchange_with_external_systems.logging_of_tasks import LogManager
from model_app.waste import WASTE_SITE_CATEGORY_YARD
from model_app.waste.models import Container, WasteSite, ContainerType, ContainerAssignment, ContainerCapacity
from workflow.models import DocStatus

total_sites = 0
new_containers = 0


@dataclass(init=True)
class OdsContainerData:
    area: Optional[int] = None
    msk_point: Optional[tuple] = None
    wgs84_point: Optional[GeoPoint] = None
    object_id: Optional[str] = None
    in_yard: Optional[int] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    address_list: Optional[list] = None
    coating_type: Optional[str] = None
    coating_group: Optional[str] = None
    container_type: Optional[str] = None
    abutment_type_list: Optional[str] = None
    ogh_object_type: Optional[str] = None
    is_separate_garbage_collection: Optional[str] = None
    imported_container: Optional[Container] = None
    new_waste_site: Optional[Union[WasteSite, bool]] = None

    def has_coords(self) -> "bool":
        return bool(self.wgs84_point)


class ImportContainerManager:
    """Фасад управляющий непосредственно импортом контейнеров"""

    def __init__(self, log_manager: "LogManager"):
        author = User.objects.get(username="admin")
        self.log_manager = log_manager
        self._geo_manager = GeoManager()
        self._mno_creator = MNOCreator(author)
        self._container_data_manager = ContainerRawDataManager(self.log_manager)
        self._need_to_created = []
        self._need_to_updated = []
        self._containers_data: "List[OdsContainerData]" = []
        try:
            self._status_demount = DocStatus.objects.get(code="demontirovano")
        except DocStatus.DoesNotExist:
            try:
                self._status_demount = DocStatus.objects.get(code="demontirovan")
            except DocStatus.DoesNotExist:
                raise RuntimeError('Не был найден статус с кодом  "demontirovano" или "demontirovan",'
                                   ' для демонтированных контейнеров.')

    def import_raw_data(self, raw_data: "List[dict]"):
        self._containers_data = self._prepare_data(raw_data)
        containers_data = self._get_containers_data_for_update()
        self.update_containers(containers_data)
        containers_data = self._get_containers_data_for_create()
        self.create_containers_and_waste_sites(containers_data)

    def create_containers_and_waste_sites(self, containers_data: "List[OdsContainerData]"):

        self.log_manager.log.info("Импорт новых контейнеров")
        n = 1
        for d in containers_data:
            if (n % 100) == 0:
                self.log_manager.log.info(f"Экспортируется контейнер {n} из {len(containers_data)}")
                self.log_manager.save_log()

            n += 1
            ws = self._geo_manager.get_nearest_waste_site(d.wgs84_point)
            self._mno_creator.set_raw_data(d)
            if not ws:
                ws = self._mno_creator.create_waste_site()
            self._mno_creator.create_container(ws)

        self.log_manager.save_log()
        self.log_manager.log.info("Сохранение новых контейнеров.")
        self._mno_creator.save_containers()

        global total_sites
        global new_containers
        self.log_manager.log.info(f"Импортировано контейнеров {len(containers_data)}")
        self.log_manager.log.info(f"Использовано уже существующих площадок {total_sites}")
        self.log_manager.log.info(f"Всего создано контейнеров {new_containers}")
        total_sites = 0
        new_containers = 0

    def update_containers(self, containers_data: "List[OdsContainerData]"):
        updated_containers = 0
        for container_data in containers_data:  # type: OdsContainerData
            if container_data.imported_container is not None and \
                    container_data.imported_container.waste_site != container_data.new_waste_site:
                container = container_data.imported_container
                waste_site = container_data.new_waste_site
                self._mno_creator.update_container(container_data, container, new_waste_site=waste_site)
                self.log_manager.log.info(f"Был перенесён контейнер с ид: {container.id} "
                                          f"на площадку {container.waste_site.id} ")
                self.log_manager.save_log()
                updated_containers += 1
        self.log_manager.log.info(f"Обновлено контейнеров {updated_containers}")

    def _get_containers_data_for_update(self) -> "List[OdsContainerData]":
        """Возвращает данные для контейнеров которые нужно обновить."""
        containers_for_update = []
        for container_data in self._containers_data:  # type: OdsContainerData
            if container_data.imported_container is not None and \
                    container_data.imported_container != container_data.new_waste_site and \
                    container_data.new_waste_site:
                containers_for_update.append(container_data)
        return containers_for_update

    def _get_containers_data_for_create(self) -> "List[OdsContainerData]":
        """Возвращает данные для контейнеров, которые нужно создать с нуля"""
        containers_for_create = []
        for container_data in self._containers_data:
            if container_data.imported_container is None:
                containers_for_create.append(container_data)
        return containers_for_create

    def demount_unnecessary_containers(self):
        """
        Демонтаж излишних контейнеров.
        Это демонтаж контейнеров, данные о которых не поступили совсем.
        """
        ods_containers_ids = [cd.object_id for cd in self._containers_data]
        already_imported_containers_ods_ids = Container.objects.filter(
            ext_id__isnull=False, external_source=ExternalSources.ODS.name).values_list("ext_id")

        demount_containers_ods_ids = []
        for already_imported_ods_id in already_imported_containers_ods_ids:
            if already_imported_ods_id not in ods_containers_ids:
                demount_containers_ods_ids.append(already_imported_ods_id)

        # поиск контейнеров для демонтажа, исключая уже демонтированные
        containers_for_demount_qs = Container.objects \
            .filter(ext_id__in=demount_containers_ods_ids, external_source=ExternalSources.ODS.name) \
            .exclude(status=self._status_demount)
        containers_for_demount_count = containers_for_demount_qs.count()
        containers_for_demount_qs.update(status=self._status_demount)
        self.log_manager.log.info(f"Демонтированные контейнеры: "
                                  f"{list(containers_for_demount_qs.values_list('id', flat=True))}")
        self.log_manager.log.info(f"Всего было демонтировано контейнеров {containers_for_demount_count}")
        self.log_manager.save_log()

    def _prepare_data(self, raw_data: "List") -> "List[OdsContainerData]":
        containers_data = self._container_data_manager.convert_raw_data(raw_data)
        count_exclude_containers = len(containers_data)
        count_exclude_containers = count_exclude_containers - len(containers_data)
        self.log_manager.log.info(f"Контейнеров не попавших в рабочую зону: {count_exclude_containers}")
        containers_data = self._container_data_manager.exclude_already_imported_containers(containers_data)
        return containers_data


class ImportMNORawDataManager:
    """Фасад управляющий загрузкой и сохранением сырых данных."""

    def __init__(self, log_manager: "LogManager"):
        self.log_manager = log_manager
        self._container_data_manager = ImportRawWasteSiteDataManager(self.log_manager)
        self._geo_manager = GeoManager()

    def import_raw_data(self, raw_data: "List[dict]"):
        containers_data: "List[WasteSiteRawData]" = self._container_data_manager.convert_raw_data(raw_data)
        for_create_list = [o for o in containers_data if not o.id]
        for_update_list = [o for o in containers_data if o.id]
        WasteSiteRawData.objects.bulk_create(for_create_list)
        self.log_manager.log.info(f"Всего было создано новых записей: {len(for_create_list)}")
        for o in for_update_list:
            o.save()
        self.log_manager.log.info(f"Было обновлено уже существующих записей: {len(for_update_list)}")
        self.rebind_nearest_mno()

    def rebind_nearest_mno(self):
        """Определяет ближайшие МНО для всех созданных сырых данных и привязывает их."""
        self.log_manager.log.info("Сканирование всех имеющихся сырых данных, и поиск ближайших МНО к ним.")
        total_rebinding_mno: int = 0
        for raw_data in WasteSiteRawData.objects.all().iterator(1000):  # type: WasteSiteRawData
            old_mno = raw_data.nearest_mno
            nearest_mno = self._geo_manager.get_nearest_waste_site(GeoPoint(float(raw_data.lat), float(raw_data.lon)))
            if old_mno != nearest_mno:
                raw_data.nearest_mno = nearest_mno
                raw_data.save()
                total_rebinding_mno += 1
                if not nearest_mno.external_source and nearest_mno.ext_id:
                    nearest_mno.external_source = ExternalSources.ODS.code
                    nearest_mno.ext_id = raw_data.object_id
                    nearest_mno.save()
        self.log_manager.log.info(f"Количество данных у которых изменилась привязка к МНО: {total_rebinding_mno}.")


ogh_types = {}
без_координат = 0


class ContainerRawDataManager:
    """
    Преобразовывает полученные данные к виду, доступному для дальнейшей обработки.
    Заметки, спустя время оказалось, что в исходном реестре контейнеры -- это МНО.
    """

    def __init__(self, log_manager: "LogManager"):
        self._geo_manager = GeoManager()
        self.log_manager = log_manager
        self._converter = self._create_converter()

    def _create_converter(self):
        return WasteSiteNamedTupleConverter()

    def convert_raw_data(self, raw_container_data: "List[dict]") -> "List[OdsContainerData]":
        """Преобразует сырые данные к ожидаемому формату, для сохранения в бд или дальнейшей обработки"""
        converted_data_list = []
        self.log_manager.log.info("Подготовка полученных данных.")

        count = 0
        for mno_dict in raw_container_data:
            t = mno_dict.get("ogh_object_type_id", {}).get("ogh_object_type", None)
            c = ogh_types.get(t, 0)
            c += 1
            ogh_types[t] = c

            count += 1
            if (count % 1000) == 0:
                self.log_manager.log.info(f"Подготовка. Обработано {count} из {len(raw_container_data)}.")
                self.log_manager.save_log()
            try:
                if not self.is_container_data(mno_dict):
                    if (count % 100) == 0:
                        self.log_manager.log.info(f"Была отброшена запись не являющаяся контейнером \n {mno_dict}")
                    continue  # Если это не контейнер, то следующая запись
                converted_data = self._converter.convert_raw_data(mno_dict)
                if converted_data.has_coords():
                    converted_data_list.append(converted_data)
                else:
                    continue
            except KeyError:
                continue
        self.log_manager.log.info(f"Количество подходящих для обработки данных: "
                                  f"{len(converted_data_list)} из {len(raw_container_data)}")
        self.log_manager.save_log()
        return converted_data_list

    def exclude_already_imported_containers(
            self, containers_data: "List[OdsContainerData]") -> "List[OdsContainerData]":
        """
        Исключает данные уже имеющихся в бд контейнеров, которые не нужно обновлять,
        то есть они не меняли своего местоположения.
        """
        z = time.time()
        objects_ids = [d.object_id for d in containers_data]
        already_imported_containers = Container.objects.filter(
            ext_id__in=objects_ids, external_source=ExternalSources.ODS.name)
        already_imported_containers = list(already_imported_containers)

        self.log_manager.log.info("Сканирование на наличие уже импортированных раннее контейнеров.")
        filtered_data = []
        number_of_exists_containers = 0
        need_to_update_containers = 0
        for d in containers_data:
            for c in already_imported_containers:
                if d.object_id == c.ext_id:
                    geo_point = GeoPoint(d.wgs84_point.latitude, d.wgs84_point.longitude)
                    waste_site_potentially_new = self._geo_manager.get_nearest_waste_site(geo_point)
                    waste_site_id_current = c.waste_site_id
                    d.imported_container = c
                    if waste_site_potentially_new and waste_site_id_current != waste_site_potentially_new.id:
                        d.new_waste_site = waste_site_potentially_new
                        filtered_data.append(d)
                        need_to_update_containers += 1
                    elif not waste_site_potentially_new:  # это тоже смена местоположения но площадку нужно создать
                        d.new_waste_site = True
                        filtered_data.append(d)
                        need_to_update_containers += 1
                    else:
                        number_of_exists_containers += 1
                else:
                    # Если площадка уже существует, но обновлять её не надо, то можно пропустить
                    # так-как обработка ей не требуется.
                    pass
            else:
                # Площадка не была найдена в уже импортированных контейнерах
                filtered_data.append(d)

        self.log_manager.log.info(f"Было отброшено {number_of_exists_containers}, экспортированных ранее контейнеров.")
        self.log_manager.log.info(f"Контейнеров имеющих новое местоположение: {need_to_update_containers}.")
        self.log_manager.log.info(f"Фильтрация выполнилась за {time.time() - z}.")
        self.log_manager.save_log()
        return filtered_data

    def is_container_data(self, raw_data_dict: "dict") -> "bool":
        ogh_obj_type: "str" = raw_data_dict.get("ogh_object_type_id", {}).get("ogh_object_type")
        if ogh_obj_type.lower() != "container":
            b = False
        else:
            b = True
        return b

    def exclude_containers_outside_working_area(
            self, containers_data: "List[OdsContainerData]") -> "List[OdsContainerData]":
        containers_data = self._geo_manager.exclude_containers_outside_working_area(containers_data)
        return containers_data


class ImportRawWasteSiteDataManager(ContainerRawDataManager):

    def _create_converter(self):
        return WasteSiteRawDataConverter()

    def convert_raw_data(self, raw_data_dict: "List[dict]") -> "List[WasteSiteRawData]":
        # noinspection PyTypeChecker
        return super().convert_raw_data(raw_data_dict)

    def exclude_already_imported_containers(self, waste_sites: "List[WasteSiteRawData]") -> "List[WasteSiteRawData]":
        """
        Исключает данные которые уже сохранены в БД и не содержат новых изменений.
        """
        start = time.time()
        objects_ids = [ws.object_id for ws in waste_sites]
        already_imported_waste_sites = WasteSiteRawData.objects.filter(object_id__in=objects_ids)
        already_imported_waste_sites = list(already_imported_waste_sites)

        self.log_manager.log.info("Сканирование на наличие уже импортированных раннее МНО.")
        exclude_waste_sites = []
        raw_datas_for_creating = []
        raw_datas_for_updating = []

        for new_ws_data in waste_sites[:]:
            for saved_ws in already_imported_waste_sites:  # type: WasteSiteRawData
                if saved_ws.object_id == new_ws_data.object_id:
                    if saved_ws.has_equal_raw_data(new_ws_data):
                        waste_sites.remove(new_ws_data)
                        exclude_waste_sites.append(saved_ws)
                    else:
                        saved_ws.update_obj_data(new_ws_data)
                        waste_sites.remove(new_ws_data)
                        raw_datas_for_updating.append(saved_ws)
                    break
                else:
                    continue
            else:
                raw_datas_for_creating.append(new_ws_data)

        self.log_manager.log.info(f"Было отброшено {len(exclude_waste_sites)}, экспортированных ранее МНО.")
        self.log_manager.log.info(f"МНО имеющих изменившиеся данные: {len(raw_datas_for_updating)}.")
        self.log_manager.log.info(f"Фильтрация выполнилась за {time.time() - start}.")
        self.log_manager.save_log()
        return raw_datas_for_creating + raw_datas_for_updating


class AbstractRawDataConverter(metaclass=ABCMeta):

    def __init__(self):
        self._geo_manager = GeoManager()

    @abstractmethod
    def convert_raw_data(self, raw_data_dict) -> "Union[OdsContainerData, WasteSiteRawData]":
        pass

    def _get_coordinates(self, raw_data_dict: "dict") -> "Optional[tuple]":
        geometry_type: "str" = raw_data_dict.get("geometry", {}).get("type", "")
        coordinates = raw_data_dict.get("geometry", {}).get("coordinates", [])
        if not coordinates:
            return None
        if geometry_type.lower() == "point":
            msk_point = coordinates
        elif geometry_type.lower() == "polygon":
            msk_point = self._get_average_coordinates(coordinates[0])
        elif geometry_type.lower() == "multipolygon":
            avg_coords_list = []
            for polygon_list in coordinates[0]:
                # polygon_list = polygon_list[0]
                print("polygon_list", polygon_list)
                t = self._get_average_coordinates(polygon_list)
                avg_coords_list.append(t)
            msk_point = self._get_average_coordinates(avg_coords_list)
        else:
            msk_point = None
        return msk_point

    def _get_average_coordinates(self, coordinates: "List[Tuple[float,float]]"):
        if not coordinates:
            raise RuntimeError()
        avg_x = statistics.mean(coord[0] for coord in coordinates)
        avg_y = statistics.mean(coord[1] for coord in coordinates)
        return avg_x, avg_y

    def _get_lat_lon_msk_point(self, raw_data_dict) -> "Tuple[GeoPoint, Optional[Tuple[float, float]]]":
        """Возвращает координаты в мировой системе, и в местной."""
        msk_point = self._get_coordinates(raw_data_dict)
        if msk_point:
            lat, lon = self._geo_manager.msk_coordinates_to_degrees(msk_point[0], msk_point[1])
        else:
            lat = None
            lon = None
        return GeoPoint(lat, lon), msk_point


class WasteSiteNamedTupleConverter(AbstractRawDataConverter):

    def convert_raw_data(self, raw_data_dict: "dict") -> OdsContainerData:
        geo_point, msk_point = self._get_lat_lon_msk_point(raw_data_dict)

        t = OdsContainerData(
            area=raw_data_dict.get("area", None),
            msk_point=msk_point,
            wgs84_point=geo_point,
            object_id=str(raw_data_dict["object_id"]),
            in_yard=raw_data_dict.get("in_yard"),
            start_date=raw_data_dict["start_date"],
            end_date=raw_data_dict["end_date"],
            address_list=raw_data_dict.get("address_list"),
            coating_type=raw_data_dict.get("coating_type_id", {}).get("coating_type"),
            coating_group=raw_data_dict.get("coating_group_id", {}).get("coating_group"),
            container_type=raw_data_dict.get("container_type_id", {}).get("container_type"),
            abutment_type_list=raw_data_dict.get("abutment_type_list", None),
            ogh_object_type=raw_data_dict["ogh_object_type_id"]["ogh_object_type"],
            is_separate_garbage_collection=raw_data_dict.get("is_separate_garbage_collection"),
            imported_container=None,
            new_waste_site=None,
        )
        return t


class WasteSiteRawDataConverter(AbstractRawDataConverter):
    """
    Сохраняет получаемые данные в json-формате, в нашей БД.
    В дальнейшем, менеджеры смотрят по координатам и сопоставляют с существующими МНО в нашей БД,
    таким образом избегая некоторого хаоса.
    """
    _created_waste_site_raw_data: "Optional[list]" = None

    def _get_all_waste_site_raw_data(self):
        if self._created_waste_site_raw_data is not None:
            return self._created_waste_site_raw_data
        else:
            self._created_waste_site_raw_data = list(WasteSiteRawData.objects.all())
            return self._created_waste_site_raw_data

    def _get_obj_by_object_id(self, object_id) -> Optional[WasteSiteRawData]:
        for obj in self._get_all_waste_site_raw_data():
            if obj.object_id == object_id:
                return obj
        else:
            return None

    def convert_raw_data(self, raw_data_dict) -> "WasteSiteRawData":
        geo_point, _ = self._get_lat_lon_msk_point(raw_data_dict)
        o = self._get_obj_by_object_id(raw_data_dict["object_id"])
        if o is None:
            o = WasteSiteRawData(
                lat=geo_point.latitude,
                lon=geo_point.longitude,
                raw_data=raw_data_dict,
                object_id=str(raw_data_dict["object_id"])
            )
        else:
            o.lat = geo_point.latitude
            o.lon = geo_point.longitude
            o.raw_data = raw_data_dict
        return o


class GeoManager:
    """Производит операции с координатами."""

    def __init__(self):
        self._waste_site_finder = WasteSiteFinder()
        self._wsg84 = pyproj.Proj("EPSG:4326")
        self._msk6335000 = pyproj.Proj(
            "+proj=tmerc +lat_0=55.66666666667 +lon_0=37.5 +k=1 +x_0=16.098 +y_0=14.512"
            " +ellps=bessel +towgs84=316.151,78.924,589.650,-1.57273,2.69209,2.34693,8.4507"
            " +units=m +no_defs"
        )

        class WorkingArea:
            TOP_LEFT = GeoPoint(55.6462198, 37.5329625)
            BOTTOM_RIGHT = GeoPoint(55.6421873, 37.5408403)

        self._working_area = WorkingArea()

    def msk_coordinates_to_degrees(self, x, y):
        lat, lon = pyproj.transform(self._msk6335000, self._wsg84, x, y)
        return lat, lon

    def get_nearest_waste_site(self, point: "GeoPoint") -> "Optional[WasteSite]":
        """Ищет ближайшие площадки в радиусе 30 метров."""
        global total_sites
        self._waste_site_finder.set_point_for_analyze(point)
        waste_sites = self._waste_site_finder.find_nearby_locations(30)
        waste_sites = list(waste_sites)
        total_sites += len(waste_sites)

        distances = []
        if len(waste_sites) > 1:
            for ws in waste_sites:
                ws_point = GeoPoint(float(ws.lat), float(ws.lon))
                distance = utilites.accurate_calculate_distance(point_from=point, point_to=ws_point)
                distances.append((distance, ws))
            distances = sorted(distances, key=lambda x: x[0])
            nearest_waste_site = distances[0][1]  # Площадка из самого первого кортежа
        elif len(waste_sites) == 1:
            nearest_waste_site = waste_sites[0]
        else:
            nearest_waste_site = None

        return nearest_waste_site

    def exclude_containers_outside_working_area(
            self, containers_data: "List[OdsContainerData]") -> "List[OdsContainerData]":
        """
        Отбрасывает контейнеры не попадающие в рабочую область.
        Рабочая область понадобилась для демонстрации фукционала. Функционал нужно
        продемонстрировать так, чтобы испытания случайно не испортили импортированные
        вручную контейнеры.
        """
        containers_in_square = []
        for container in containers_data:  # type: OdsContainerData
            lat = container.wgs84_point.latitude
            lon = container.wgs84_point.longitude
            if (self._working_area.TOP_LEFT.latitude > lat > self._working_area.BOTTOM_RIGHT.latitude and
                    self._working_area.TOP_LEFT.longitude < lon < self._working_area.BOTTOM_RIGHT.longitude):
                containers_in_square.append(container)
        return containers_in_square


class MNOCreator:
    """Создаёт МНО и контейнеры"""
    _raw_d: "OdsContainerData"  # raw_data

    def __init__(self, author: Optional[User] = None):
        self._new_containers = []
        self.log = logging.getLogger("ods_integration")
        self.author = author
        self.waste_site_status_ne_provereno = DocStatus.objects.get(code="ne-provereno")
        self.container_status_ne_provereno = DocStatus.objects.get(code="ne-proveren")

    def set_raw_data(self, raw_data: "OdsContainerData"):
        self._raw_d = raw_data

    def create_waste_site(self):
        waste_site = WasteSite(
            author=self.author,
            comment="МНО создано в рамках интеграции с АСУ_ОДС, т.к. в радиусе 30 м от контейнера в ЭМТСОО нет МНО",
            participant=None,
            ro_zone=None,
            borough=None,
            area=None,
            category=WASTE_SITE_CATEGORY_YARD,
            ext_id=None,
            external_source=ExternalSources.ODS.name,
            lon=self._raw_d.wgs84_point.longitude,
            lat=self._raw_d.wgs84_point.latitude,
            position=geos.Point(x=self._raw_d.wgs84_point.longitude, y=self._raw_d.wgs84_point.latitude, srid=4326),
            address=None,
            coordinates_approved=False,
            qhash=None,
            status=self.waste_site_status_ne_provereno,
            is_tmp=False,
            date_add=None,
            date_remove=None,
            waste_mass=0,
            waste_volume=0,
            photo=None,
            schedule_text=None,
            deleted=True,
        )
        waste_site.save()
        return waste_site

    def create_container(self, waste_site: "Optional[WasteSite]"):
        if not waste_site:
            waste_site = self.create_waste_site()

        c = Container(
            type=self._get_container_type(),
            assignment=self._get_container_assignment(),
            capacity=None,
            waste_site=waste_site,
            status=self.container_status_ne_provereno,
            number=None,
            participant=None,
            comment="Выгрузка из АСУ ОДС",
            volume_sensor_uid=None,
            rfid=None,
            ext_id=self._raw_d.object_id,
            external_source=ExternalSources.ODS.name,
            deleted=True,
        )
        self._new_containers.append(c)
        global new_containers
        new_containers += 1
        self._raw_d = None
        return c

    def update_container(self, container_data: "OdsContainerData", container: "Container",
                         new_waste_site: "Union[bool,WasteSite]"):
        """
        На текущий момент обновляет только площадку, на которой расположен контейнер,
        если она была изменена. Но предполагаю, что в будущем, изменяться может больше данных.
        """
        self.set_raw_data(container_data)
        if new_waste_site is True:
            new_waste_site = self.create_waste_site()
        elif container.waste_site == new_waste_site:
            raise RuntimeError("Данные контейнера обновлять не нужно, так-как его местоположение не изменилось.")
        container.waste_site = new_waste_site
        container.save()
        self._raw_d = None

    def save_containers(self):
        Container.objects.bulk_create(self._new_containers, batch_size=500)

    @lru_cache
    def _get_container_type(self):
        ct = ContainerType.objects.get(id=3)
        return ct

    @lru_cache
    def _get_container_assignment(self) -> "ContainerAssignment":
        ca = ContainerAssignment.objects.get(id=1)
        return ca

    @lru_cache
    def _get_capacity(self):
        cc = ContainerCapacity.objects.get(id=2)
        return cc


class WasteSiteFinder(AbstractNearestLocationFinder):

    def search_nearby_locations_with_square(self, lat_start, lat_end, lon_start, lon_end):
        sites = WasteSite.objects.filter(lat__range=(lat_start, lat_end), lon__range=(lon_start, lon_end))
        return sites


class WasteSiteFinderTemp(AbstractNearestLocationFinder):
    d_start = datetime.date(year=2021, month=12, day=1)
    d_end = datetime.date(year=2021, month=12, day=31)

    def search_nearby_locations_with_square(self, lat_start, lat_end, lon_start, lon_end):
        sites = WasteSite.objects.filter(
            lat__range=(lat_start, lat_end),
            lon__range=(lon_start, lon_end)
        ).only("lat", "lon", "participant_id", "ext_id", "external_source")
        return sites
