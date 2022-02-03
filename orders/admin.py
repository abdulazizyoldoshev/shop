from django.contrib import admin
from .models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    search_fields = ['user', 'product']
    list_filter = ['user', 'product']
    list_display =['user', 'product']
    autocomplete_fields = ['product']
    # Register your here.
