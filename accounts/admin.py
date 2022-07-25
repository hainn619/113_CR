from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from .form import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form= CustomUserChangeForm
    model= CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "department")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "department")}),
    )
    list_display = [
        "username", "email", "first_name", "last_name", "role", "department", "is_staff",
    ]

admin.site.register(CustomUser, CustomUserAdmin)