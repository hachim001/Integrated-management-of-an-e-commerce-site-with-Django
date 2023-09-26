from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

class Category(models.Model):
    name = models.CharField(max_length=100)
    date_creation = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='store/images/%Y/%m/%d',null=True)
    image1 = models.ImageField(upload_to='store/images/%Y/%m/%d',null=True)
    image2 = models.ImageField(upload_to='store/images/%Y/%m/%d',null=True)
    image3 = models.ImageField(upload_to='store/images/%Y/%m/%d',null=True)


    date_creation = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name_plural="Products"
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.main_image.url))
    def __str__(self):
        return self.title
