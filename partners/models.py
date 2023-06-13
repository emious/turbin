from django.db import models


# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    short_desc = models.TextField()
    desc = models.TextField()
    thumbnail = models.ImageField(upload_to='images/partners', blank=True, null=True)

    def __str__(self):
        return self.name

