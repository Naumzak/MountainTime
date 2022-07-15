from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Backpack(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)