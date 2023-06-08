from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    short_desc = models.TextField()
    desc = models.TextField()
    thumbnail_1 = models.ImageField(upload_to='images/products', blank=True, null=True)
    thumbnail_2 = models.ImageField(upload_to='images/products', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)



    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='images/categories', blank=True, null=True)
    short_desc = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name
