from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from import_export.admin import ImportExportModelAdmin

from .profile_inline import ProfileInline

User = get_user_model()

try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
    inlines = [ProfileInline]
