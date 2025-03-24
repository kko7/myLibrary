from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'name', 'is_staff', 'is_active', 'admin_level', 'is_librarian')
    list_filter = ('is_staff', 'is_active', 'admin_level', 'is_librarian')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('name', 'id_card', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'admin_level', 'is_librarian')}),
        ('Group Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'name', 'id_card', 'phone', 'admin_level', 'is_librarian', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
