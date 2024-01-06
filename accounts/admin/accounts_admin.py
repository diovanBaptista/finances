from django.contrib import admin
from django_object_actions import DjangoObjectActions
from ..models import Account
from .installment_inline import InstallmentInline

@admin.register(Account)
class AccountAdmin(DjangoObjectActions,admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'value',
        'date',
        'store'
    ]

    search_fields = [
        'id',
        'store',
    ]

    list_filter = [
        'installments'
    ]

    inlines = [InstallmentInline]

    # autocomplete_fields = [
    #     'campos_fk
    # ]

    def avancar(self, request, obj):
        obj.avancar(request)

    change_actions = ["avancar"]

    def get_change_actions(self, request, obj_id, form_url):
        try:
            obj = Account.objects.get(pk=obj_id)
            actions = []
            if obj.status not in ["Parte completada"]:
                actions.append("avancar")
            return actions
        except:
            return []

    def get_readonly_fields(self, request, obj):
        if not obj:
            return ["status"]

        if obj.status in ["Parte cadastro"]:
            return [
                "id",
                "status",
            ]
        elif obj.status in ["Parte financeira"]:
            return [
                "id",
                "status",
                'name',
                'description',
                'date',
                'store',
            ]
        elif obj.status in ["Parte completada"]:
            return [
                "id",
                "status",
                'name',
                'description',
                'date',
                'store',
                'installments',
                'value',
                'installment_number',
                'due_date_day'
            ]
        else:
            return '__all__'

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return [
                (
                    "Dados da compra",
                    {
                        "fields": [
                            'name',
                            'description',
                            'date',
                            'store',
                            'status',
                        ]
                    },
                )
            ]
        elif obj.status == 'Parte cadastro':
            return [
                (
                    "Dados da compra",
                    {
                        "fields": [
                            'name',
                            'description',
                            'date',
                            'store',
                            'status',
                        ]
                    },
                )
            ]
        elif obj.status == 'Parte financeira':
            return [
                (
                    "Dados da compra",
                    {
                        "fields": [
                            'id',
                            'name',
                            'description',
                            'date',
                            'store',
                            'status',
                        ]
                    },
                ),
                (
                    "Dados financeiros",
                    {
                        "fields": [
                            'installments',
                            'value',
                            'due_date_day',
                            'installment_number',
                        ]
                    },
                ),
            ]
        elif obj.status in ["Parte completada"]:
            return [
                (
                    "Dados da compra",
                    {
                        "fields": [
                            'id',
                            'name',
                            'description',
                            'date',
                            'store',
                            'status',
                        ]
                    },
                ),
                (
                    "Dados financeiros",
                    {
                        "fields": [
                            'installments',
                            'value',
                            'due_date_day',
                            'installment_number',
                            
                        ]
                    },
                ),
            ]
        else: 
            return '__all__'
        
    
