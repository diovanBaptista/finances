from django.contrib import admin

from ..models import TipoConta


@admin.register(TipoConta)
class TipoContaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome'
    ]

    search_fields = [
        'id',
        'nome'
    ]

    # list_filter = [
    #     'campos_fk_e_booleanos
    # ]

    # list_select_related = [
    #     'campos_dos_campos_fk
    # ]

    # autocomplete_fields = [
    #     'campos_fk
    # ]
