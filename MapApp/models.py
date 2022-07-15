import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Marker(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    color = models.CharField(max_length=50, default='red', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Маркер'
        verbose_name_plural = 'Маркеры'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Map(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    markers = models.ManyToManyField(Marker, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
