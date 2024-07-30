import time

from django.core.management import BaseCommand

from asu_ods_integration.models import AsuOdsExport
from data_exchange_with_external_systems.constants import ExternalSources
from data_exchange_with_external_systems.logging_of_tasks import LogManager
from model_app.waste.models import Container, WasteSite


class Command(BaseCommand):

    def handle(self, *args, **options):
        start = time.time()
        log_manager = LogManager("ods_integration")
        obj = AsuOdsExport.objects.create(
            command_name="delete_all_import"
        )
        log_manager.set_obj(obj)
        log_manager.log.info("Удаление импорта из АСУ ОДС началось.")
        log_manager.save_log()

        containers_exists = True
        containers_count = Container.objects.filter(external_source=ExternalSources.ODS.name).count()
        while containers_exists:
            s = time.time()
            print("Поиск контейнеров")
            ids_qs = Container.objects.filter(
                external_source=ExternalSources.ODS.name).values_list("id", flat=True)
            containers_ids = list(ids_qs)
            log_manager.log.info("Выполняется процедура удаления контейнеров")
            deleted = Container.objects.filter(id__in=containers_ids).delete()
            log_manager.log.info(f"Были удалены контейнеры {str(deleted)}, {str(time.time() - s)}")
            containers_exists = Container.objects.filter(external_source=ExternalSources.ODS.name).exists()

        log_manager.log.info(f"Удаление контейнеров выполнялось {time.time() - start}")
        log_manager.log.info(f"Были удалены контейнеры {containers_count}")
        log_manager.save_log()
        s = WasteSite.objects.filter(external_source=ExternalSources.ODS.name).delete()
        log_manager.log.info(f"Были удалены МНО {s}")
        log_manager.log.info(f"Удаление всех записей выполнялось {round(time.time() - start, 3)} секунд")
        log_manager.save_log()
