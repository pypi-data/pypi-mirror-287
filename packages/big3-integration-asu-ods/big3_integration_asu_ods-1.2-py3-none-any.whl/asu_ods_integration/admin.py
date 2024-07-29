from django.contrib import admin
from django import forms

from big3_data_main_app.custom_admin import custom_admin_site
from .models import AsuOdsExport, WasteSiteRawData


class AsuOdsExportForm(forms.ModelForm):

    log = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 147,
                   'rows': 30,
                   'readonly': 'readonly',
                   "style": """
                        font-family: monospace;
                        font-stretch: condensed; 
                        font-size: 1em;
                        white-space: pre;
                        overflow-y: scroll;
                    """
                   }
        ),
        required=False
    )
    response_raw = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': 147,
                   'rows': 10,
                   'readonly': 'readonly',
                   "style": """
                            font-family: monospace;
                            font-stretch: condensed; 
                            font-size: 1em;
                            white-space: pre;
                            overflow-y: hidden;
                        """
                   }
        ),
        required=False
    )

    class Meta:
        model = AsuOdsExport
        exclude = ("id", )


@admin.register(AsuOdsExport, site=custom_admin_site)
class AsuOdsExportAdmin(admin.ModelAdmin):
    form = AsuOdsExportForm
    list_display = ('id', 'request_id', 'datetime_create', 'datetime_update', 'command_name', 'status_of_completion',)
    fields = ("request_id", 'datetime_create', 'datetime_update', "log", "response_raw", 'status_of_completion',)
    readonly_fields = ('request_id', 'datetime_create', 'datetime_update', 'status_of_completion',)


@admin.register(WasteSiteRawData, site=custom_admin_site)
class WasteSiteRawDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_id', 'lat', 'lon', 'nearest_mno', 'datetime_create', 'datetime_update', )
    readonly_fields = ('id', 'object_id', 'nearest_mno', 'datetime_create', 'datetime_update', )
    search_fields = ('object_id', )
