import logging

from django.core.management import BaseCommand

from asu_ods_integration.import_containers import ImportMNORawDataManager
from data_exchange_with_external_systems.logging_of_tasks import LogManager


class Command(BaseCommand):

    def handle(self, *args, **options):
        import_manager = ImportMNORawDataManager(log_manager=LogManager("ods_integration"))
        import_manager.rebind_nearest_mno()
        import_manager.log_manager.finish()