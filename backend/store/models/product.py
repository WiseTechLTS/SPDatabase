from django.db import models
from .category import Category
from django.utils.safestring import mark_safe
from PIL import Image as Im




class Products(models.Model):
    name = models.CharField(max_length=60)
    price= models.FloatField(default=0.0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products();
        
     # image_tag is going to show the image in the admin panel
    def image_tag(self):  # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.image))

    # this is for a thumnail of the image in the admin panel
    def save(self):  # new
        super().save()
        img = Im.open(self.image.path)
        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
