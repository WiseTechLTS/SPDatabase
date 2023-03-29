from django import forms
from .models import Product


class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('collection', 'category', 'name', 'size', 'price', 'stock', 'url', 'image', 'imageUrl', 'body')
