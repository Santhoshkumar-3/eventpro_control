from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    list_display = ['id','username', 'email', 'first_name', 'last_name', 'is_staff', 'role']
    search_fields = ['id','username', 'email', 'first_name', 'last_name', 'role']

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
