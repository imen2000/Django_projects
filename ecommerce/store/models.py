from tabnanny import verbose
from django.db import models
from time import timezone


class Category (models.Model):
   
    name = models.CharField(
        max_length=225
        # choices=CATEGORY_CHOICES,
            )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):

    name = models.CharField(max_length=120, blank=False, null=False)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=3)
    width = models.DecimalField(max_digits=4, decimal_places=3)
    height = models.DecimalField(max_digits=4, decimal_places=3)
    depth = models.DecimalField(
        default=0, null=False, max_digits=4, decimal_places=3)
    material = models.CharField(max_length=120, null=True, blank=False)
    image = models.ImageField(default='default.jpeg', upload_to='product_pics')
    stock = models.IntegerField()

    def __str__(self):
        return self.name
