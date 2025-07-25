from django.contrib import admin

from ..models import Entrada


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'valor',
        'data'
    ]

    search_fields = [
        'id',
        'valor',
        'data'
    ]

    list_filter = [
        'tipo_entrada',
        'usuario',
    ]

    # list_select_related = [
    #     'campos_dos_campos_fk
    # ]

    autocomplete_fields = [
        'tipo_entrada',
        'usuario',
    ]
