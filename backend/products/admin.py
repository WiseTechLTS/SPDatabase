from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'size', 'price', 'in_stock', 'quantity', 'image', 'image_url', 'url', 'collection', 'category', 'body')

# Register your models here.
admin.site.register(Product, ProductAdmin)
