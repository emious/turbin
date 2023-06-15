# Generated by Django 4.2.1 on 2023-06-15 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_alter_partner_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'همکار', 'verbose_name_plural': 'همکاران'},
        ),
        migrations.AlterField(
            model_name='partner',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='توضیح'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=100, verbose_name='نام شرکت'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='short_desc',
            field=models.TextField(verbose_name='توضیح کوتاه'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/partners', verbose_name='تصویر'),
        ),
    ]
