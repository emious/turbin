from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Content(models.Model):
    STATUS = (
        (0, "پیش نویس"),
        (1, "منتشر شده")
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    short_desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    tags = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to='', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    status = models.IntegerField(choices=STATUS, default=0)

    content = RichTextField(null=True, blank=True,
                            config_name="special")

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'مطلب'
        verbose_name_plural = 'مطالب'

    def __str__(self):
        return self.title
