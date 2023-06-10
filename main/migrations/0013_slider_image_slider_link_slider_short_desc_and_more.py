# Generated by Django 4.2.1 on 2023-06-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_websitesetting_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.ImageField(default='', upload_to='images/template/main-slider', verbose_name='تصویر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='لینک'),
        ),
        migrations.AddField(
            model_name='slider',
            name='short_desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='توضیح کوتاه'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان'),
        ),
    ]