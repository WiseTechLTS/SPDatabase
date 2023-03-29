from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','image_tag', 'image', 'image_url', 'url', 'collection', 'category', 'size', 'price', 'in_stock', 'body')

# Register your models here.
admin.site.register(Product, ProductAdmin)
