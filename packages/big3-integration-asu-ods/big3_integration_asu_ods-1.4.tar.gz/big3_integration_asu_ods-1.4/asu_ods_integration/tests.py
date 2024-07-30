import datetime
from unittest import skip

from django.core.management import call_command
from django.db import connection
from django.test import TestCase

from data_exchange_with_external_systems.constants import ExternalSources
from asu_ods_integration.external.asu_ods import AsuOds
from asu_ods_integration.models import AsuOdsExport
from model_app.waste.models import WasteSite
from tests.factories import WasteSiteFactory


@skip("Возвращается 502 ошибка, при запросе токена.")
class TestGetToken(TestCase):  # Вернуть тест можно после того как починят или наши девопсы, или со стороны ДИТа

    def test_get_token(self):
        token = AsuOds.get_token()
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 50)

    def test_request_containers(self):
        import time
        time.sleep(10)
        start_dt = datetime.datetime(year=2021, month=1, day=1)
        end_dt = datetime.datetime(year=2021, month=1, day=30)
        export_obj = AsuOds.request_ogh('container', start_dt, end_dt)
        self.assertIsInstance(export_obj, AsuOdsExport)
        self.assertTrue(export_obj.request_id)


class TestCommands(TestCase):

    def setUp(self) -> None:
        WasteSiteFactory.create(external_source=ExternalSources.ODS.name)
        WasteSiteFactory.create(external_source=ExternalSources.ODS.name)
        WasteSiteFactory.create(external_source=ExternalSources.ODS.name)

    def test_command_delete_all_import(self):
        self.assertEqual(WasteSite.objects.filter(external_source=ExternalSources.ODS.name).count(), 3)
        with connection.cursor() as cursor:
            cursor.execute("REFRESH MATERIALIZED VIEW report_confirmation_dashboard")
        call_command("asu_ods_delete_all_import")
        self.assertEqual(WasteSite.objects.filter(external_source=ExternalSources.ODS.name).count(), 0)

    # Для этих тестов нужно сделать заглушку по получаемым данным
    # def test_save_raw_data_on_waste_site(self):
    #     call_command("save_raw_data_on_waste_site", start_date="2024-01-01", end_date="2024-01-02")
    #
    # def test_asu_ods_import_containers(self):
    #     call_command("asu_ods_import_containers", start_date="2024-01-01", end_date="2024-01-02")

