from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="عنوان")
    short_desc = models.TextField(verbose_name="توضیحات کوتاه")
    desc = models.TextField(verbose_name="توضیحات")
    thumbnail_1 = models.ImageField(upload_to='images/products', blank=True, null=True, verbose_name="تصویر اول")
    thumbnail_2 = models.ImageField(upload_to='images/products', blank=True, null=True, verbose_name="تصویر دوم")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="دسته بندی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="عنوان")
    thumbnail = models.ImageField(upload_to='images/categories', blank=True, null=True, verbose_name="تصویر")
    short_desc = models.TextField(null=True, blank=True, verbose_name="توضیح")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی ها'
