from django.contrib import admin

from ..models import Installment


class InstallmentInline(admin.TabularInline):
    model = Installment

    extra = 0

    readonly_fields = [
        'status',
        'accounts',
        'installment_value',
        'maturity',
    ]
