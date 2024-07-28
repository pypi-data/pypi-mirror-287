from django.urls import path, include
from .views import (AsuOdsCallbackView, import_containers_page, menu_of_commands,
                    delete_all_containers_page, delete_containers_start, import_contracts_page, import_contracts_start)

urlpatterns = [
    path("callback/",
         AsuOdsCallbackView.as_view()
         ),
    path("import_containers/<str:command_name>/",
         import_containers_page,
         name="asu_ods_import_containers_page"
         ),
    path("menu_of_commands/",
         menu_of_commands,
         name="asu_ods_menu_of_commands"
         ),
    path("delete_containers/",
         delete_all_containers_page,
         name="asu_ods_delete_containers_page"
         ),
    path("delete_containers_start/",
         delete_containers_start,
         name="asu_ods_delete_containers_start"
         ),
    path("import_contracts/",
         import_contracts_page,
         name="asu_ods_import_contracts_page"
         ),
    path("import_contracts_start/",
         import_contracts_start,
         name="asu_ods_import_contracts_start"
         ),
]
