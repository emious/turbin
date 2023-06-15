from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from extension.utils import jalali_converter

# Create your models here.

class Content(models.Model):
    STATUS = (
        (0, "پیش نویس"),
        (1, "منتشر شده")
    )

    title = models.CharField(max_length=200, unique=True, verbose_name="عنوان")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="پیوند")
    short_desc = models.TextField(verbose_name="توضیحات کوتاه")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="نویسنده")
    tags = models.TextField(null=True, blank=True, verbose_name="تگ ها")
    thumbnail = models.ImageField(upload_to='', blank=True, null=True, verbose_name="تصویر")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    status = models.IntegerField(choices=STATUS, default=0, verbose_name="وضعیت انتشار")

    content = RichTextField(null=True, blank=True,
                            config_name="special",
                            verbose_name="توضیحات")

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'مطلب'
        verbose_name_plural = 'مطالب'

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.updated_on)

    jpublish.short_description = "زمان انتشار"
