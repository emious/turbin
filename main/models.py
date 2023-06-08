import os

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe


from django.conf import settings


class Slider(models.Model):
    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self



class NavMenu(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    link = models.URLField(default='', verbose_name='لینک')

    class Meta:
        verbose_name = 'منو'
        verbose_name_plural = 'منو ها'

    def __str__(self):
        return self.name


class WebsiteSetting(models.Model):

    phone_number = models.CharField(max_length=12, default='', blank=True, verbose_name='شماره تلفن')
    email = models.CharField(max_length=30, default='', blank=True, verbose_name='ایمیل')
    address = models.CharField(max_length=50, default='', blank=True, verbose_name='آدرس')
    work_time = models.CharField(max_length=30, default='', blank=True, verbose_name='ساعت کاری')
    about = models.TextField(default='', blank=True, verbose_name='درباره ما')
    favicon = models.ImageField(upload_to='images/template/', blank=True, verbose_name='ایکن')
    footer_logo = models.ImageField(upload_to='images/template/', blank=True, verbose_name='لوگو فوتر')
    logo = models.ImageField(upload_to='images/template/', blank=True, verbose_name='لوگو')
    logo_small = models.ImageField(upload_to='images/template/', blank=True, verbose_name='لوگو کوچک')

    # def image_tag(self):
    #     return mark_safe('<img src="media/%s" width="150" height="150" />' % self.favicon)

    def image_tag(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width: 200px; height:70px;" />' % self.logo.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'لوگو'

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


    def save(self, *args, **kwargs):
        if not self.pk and WebsiteSetting.objects.exists():
            # if you'll not check for self.pk
            # then error will also be raised in the update of exists model
            raise ValidationError('There is can be only one JuicerBaseSettings instance')
        return super(WebsiteSetting, self).save(*args, **kwargs)
