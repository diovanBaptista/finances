from django.contrib import admin

from ..models import ContaMensais


@admin.register(ContaMensais)
class ContaMensaisAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'valor',
        'data'
    ]

    search_fields = [
        'id',
        'valor',
    ]

    list_filter = [
        'conta'
    ]

    # list_select_related = [
    #     'campos_dos_campos_fk
    # ]

    autocomplete_fields = [
        'conta',
        'owner'
    ]
