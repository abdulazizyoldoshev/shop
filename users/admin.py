from django.contrib import admin
from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name']


# Register your models here.
