from django.contrib import admin
from products.models import ProductModel, CategoryModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['number', 'email', 'username']
    list_filter = ['number', 'email', 'username']
    list_display = ['number', 'email', 'username']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']
    list_display = ['name']

# Register your models here.
