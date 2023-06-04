import os

from django.core.exceptions import ValidationError
from django.db import models

from django.conf import settings


class Slider(models.Model):
    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدر'


class HeaderMenu:
    class Meta:
        verbose_name = 'منو'
        verbose_name_plural = 'منو ها'

    name = models.CharField(max_length=50),
    link = models.SlugField(),



class WebsiteSetting(models.Model):

    phone_number = models.CharField(max_length=12, default='', blank=True)
    email = models.CharField(max_length=30, default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    work_time = models.CharField(max_length=30, default='', blank=True)
    about = models.TextField(default='', blank=True)
    favicon = models.ImageField(upload_to='images/template/', blank=True)
    footer_logo = models.ImageField(upload_to='images/template/', blank=True)
    logo = models.ImageField(upload_to='images/template/', blank=True)
    logo_small = models.ImageField(upload_to='images/template/', blank=True,)



    
    def save(self, *args, **kwargs):
        if not self.pk and WebsiteSetting.objects.exists():
            # if you'll not check for self.pk
            # then error will also be raised in the update of exists model
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(WebsiteSetting, self).save(*args, **kwargs)
