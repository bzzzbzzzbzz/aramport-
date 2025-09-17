from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'currency', 'in_stock', 'category')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'in_stock', 'category')
    list_filter = ('category', 'in_stock')
    search_fields = ('name', 'description')