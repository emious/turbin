import os

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import mark_safe


from django.conf import settings


class Slider(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100, verbose_name='عنوان')
    short_desc = models.CharField(blank=True, null=True, max_length=100, verbose_name='توضیح کوتاه')
    link = models.URLField(blank=True, null=True, verbose_name='لینک')
    image = models.ImageField(upload_to='images/template/main-slider', verbose_name='تصویر')


    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title



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
    address = models.CharField(max_length=70, default='', blank=True, verbose_name='آدرس')
    work_time = models.CharField(max_length=30, default='', blank=True, verbose_name='ساعت کاری')
    about = models.TextField(default='', blank=True, verbose_name='درباره ما')
    desc = models.TextField(default='', verbose_name='توضیحات اضافه')
    favicon = models.ImageField(upload_to='images/template/', blank=True, verbose_name='ایکن')
    footer_logo = models.ImageField(upload_to='images/template/', blank=True, verbose_name='لوگو فوتر')
    logo = models.ImageField(upload_to='images/template/', blank=True, verbose_name='لوگو')
    logo_small = models.ImageField(upload_to='images/template/', blank=True, verbose_name='لوگو کوچک')

    # def image_tag(self):
    #     return mark_safe('<img src="media/%s" width="150" height="150" />' % self.favicon)

    def image_tag(self):
        if self.logo_small:
            return mark_safe('<img src="%s" style="width: 200px; height:70px;" />' % self.logo_small.url)
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
