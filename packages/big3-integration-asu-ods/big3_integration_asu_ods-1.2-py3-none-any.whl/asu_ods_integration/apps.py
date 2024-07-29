from functools import lru_cache

from django.apps import AppConfig
from django.urls import reverse


class AsuOdsIntegrationConfig(AppConfig):
    name = 'asu_ods_integration'
    verbose_name = "Интеграция с АСУ ОДС"
    additional = True

    def additional_features_url(self):
        url = reverse("asu_ods_menu_of_commands")
        return url
