from django.db import models


# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="نام شرکت")
    short_desc = models.TextField(verbose_name="توضیح کوتاه")
    desc = models.TextField(blank=True, null=True, verbose_name="توضیح")
    thumbnail = models.ImageField(upload_to='images/partners', blank=True, null=True, verbose_name="تصویر")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'همکار'
        verbose_name_plural = 'همکاران'

