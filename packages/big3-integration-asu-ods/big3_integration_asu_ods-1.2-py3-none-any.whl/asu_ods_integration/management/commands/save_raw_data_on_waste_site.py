import os
from typing import List

from asu_ods_integration.import_containers import ImportMNORawDataManager
from asu_ods_integration.models import AsuOdsExport

from asu_ods_integration.management.commands.asu_ods_import_containers import (
    Command as ImportContainersCommand
)


class Command(ImportContainersCommand):
    _mno_raw_data: "List" = None
    _export_obj: "AsuOdsExport" = None

    def _create_import_manager(self) -> "ImportMNORawDataManager":
        return ImportMNORawDataManager(self._log_manager)

    @property
    def command_name(self):
        s = os.path.basename(__file__).split(".")[0]
        return s
