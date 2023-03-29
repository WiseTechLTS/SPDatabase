from django.db import models
from authentication.models import User
from django.utils.safestring import mark_safe
from PIL import Image as Im
# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<
def upload_to(instance, filename):
    return f'/{filename}'

class Product(models.Model):
    CATEGORY = (
        ('T-Shirt', 'T-Shirt'),
        ('Hoodie', 'Hoodie'),
        ('Shorts', 'Shorts'),
        ('Stickers', 'Stickers'),
        ('Sporting Goods', 'Sporting Goods'),
    )



    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
        ('XXL', 'Ttiple Extra Large'),
    )

    COLLECTION = (
        ('Fight Gear', 'Fight Gear'),
        ('Street Wear Clothing', 'Street Wear Clothing'),
        ('Home Page', 'Home Page'),
    )

    NAME = (
        ('Scrap Poverty', 'Scrap Poverty'),
        ('The Way - Addicted to the Mat (Coach Bollinger)',
         'The Way - Addicted to the Mat (Coach Bollinger)'),
        ("The Original Fighter's Voice & Scrap Soldier Collaboration Long Sleeve Shirt",
         "The Original Fighter's Voice & Scrap Soldier Collaboration Long Sleeve Shirt"),
        ("The Original Fighter's Voice & Scrap Solider Collaboration Short Sleeve Shirt",
         "The Original Fighter's Voice & Scrap Solider Collaboration Short Sleeve Shirt"),
        ("The Original Fighter's Voice & Scrap Soldier Collaboration Pullover Hoodie",
         "The Original Fighter's Voice & Scrap Soldier Collaboration Pullover Hoodie"),
        ("North County MMA & Scrap Solider Collaboration Shirt",
         "North County MMA & Scrap Solider Collaboration Shirt"),
        ("Vale Tudo Shorts", "Vale Tudo Shorts"),
        ("MMA Shorts (4 Way Stretch)", "MMA Shorts (4 Way Stretch)"),
        ("Crop Hoodie For Woman", "Crop Hoodie For Woman"),
        ("Star Logo Sticker",  "Star Logo Sticker"),
        ("Slant T-Shirt (Hottest Selling)", "Slant T-Shirt (Hottest Selling)"),
        ("Vertical Flag 1 Color", "Vertical Flag 1 Color"),
        ("Military Style Ribbon Hoodie", "Military Style Ribbon Hoodie"),
    )

    PRICE = (
        (3.00, 3.00),
        (15.00, 15.00),
        (20.00, 20.00),
        (22.50, 22.50),
        (25.00, 25.00),
        (27.50, 27.50),
        (29.00, 29.00),
        (29.95, 29.95),
        (32.50, 32.50),
        (39.95, 39.95),
    )

    URL = (
        ('The Way', "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-way-addicted-to-the-mat-coach-bollinger"),
        ('Scrap Poverty', "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/scrap-poverty"),
        ('The Way', "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-way-addicted-to-the-mat-coach-bollinger"),
        ("The Original Fighter's Voice & Scrap Soldier Collaboration Long Sleeve Shirt",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-original-fighters-voice-scrap-soldier-collaboration-long-sleeve-shirt"),
        ("The Original Fighter's Voice & Scrap Solider Collaboration Short Sleeve Shirt",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-original-fighters-voice-and-scrap-solider-collaboration-shirt-short-sleeve"),
        ("The Original Fighter's Voice & Scrap Soldier Collaboration Pullover Hoodie",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-original-fighters-voice-scrap-soldier-collaboration-pullover-hoodie"),
        ("North County MMA & Scrap Solider Collaboration Shirt",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/north-county-mma-scrap-solider-collaboration-shirt"),
        ("Vale Tudo Shorts", "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/vale-tudo-shorts"),
        ("MMA Shorts (4 Way Stretch)",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/mma-shorts"),
        ("Crop Hoodie For Woman",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/crop-hoodie-for-woman"),
        ("Star Logo Sticker",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/star-sticker"),
        ("Slant T-Shirt (Hottest Selling)",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/slant-t-shirt"),
        ("Vertical Flag 1 Color",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/destroy-your-demons"),
        ("Military Style Ribbon Hoodie",
         "https://scrap-soldier-clothing-fight-gear.myshopify.com/products/military-style-ribbon-hoodie"),
    )




    user = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
    ## <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<
    collection = models.CharField(max_length=25, unique=True, default='Fight Gear', choices=COLLECTION)
    # collection is Fight Gear, Street Wear Clothing and Home Page
    category = models.CharField(max_length=25, unique=True, default='T-Shirts', choices=CATEGORY)
    # category is T-Shirts, Hoodies, Shorts, etc.
    name = models.CharField(max_length=100, unique=True, default='Scrap Poverty', choices=NAME)
    # name is the name of the product
    size = models.CharField(max_length=4, choices=SHIRT_SIZES, default='S')
    # size is the size of the product
    price = models.FloatField(max_length=5, unique=True, choices=PRICE)
    # price is the price of the product
    in_stock = models.BooleanField(default=True)
    # in_stock is a boolean to check if the product is in stock
    url = models.URLField(max_length=200, unique=True, choices=URL)
    # url is the url of the product
    image = models.ImageField(upload_to='images', blank=True)
    # image is the image of the product
    image_url = models.URLField(max_length=200, unique=True)
    # image_url is the url of the image of the product
    body = models.TextField(max_length=1000)

    # image_tag is going to show the image in the admin panel
    def image_tag(self):  # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.image))

    # this is for a thumnail of the image in the admin panel
    def save(self): # new
        super().save()
        img = Im.open(self.image.path)
        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)