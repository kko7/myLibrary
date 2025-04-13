from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'name', 'admin_level', 'is_librarian', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'admin_level', 'is_librarian')
    search_fields = ('username', 'email', 'name', 'id_card')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'id_card', 'email', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Custom Fields'), {'fields': ('admin_level', 'is_librarian')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'admin_level', 'is_librarian'),
        }),
    )