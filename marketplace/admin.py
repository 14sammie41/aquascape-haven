from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_price')

admin.site.register(Product, ProductAdmin)
