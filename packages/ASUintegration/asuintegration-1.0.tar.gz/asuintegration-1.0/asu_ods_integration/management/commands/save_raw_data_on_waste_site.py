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

from integrations.asu_ods_integration.exceptions import RequestError
from integrations.asu_ods_integration.import_containers import ImportContainerManager, ImportMNORawDataManager
from integrations.asu_ods_integration.models import AsuOdsExport, StatusesOfCompletions
from integrations.asu_ods_integration.external.asu_ods import AsuOds
from integrations.logging_of_tasks import LogManager

from integrations.asu_ods_integration.management.commands.asu_ods_import_containers import (
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
