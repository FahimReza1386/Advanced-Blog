# Django Imports
from django.contrib import admin

# Locale Imports
from accounts.models.user import UserModel
from accounts.models.profile import ProfileModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active', 'is_staff')
    search_fields = ('email',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('-created_at',)