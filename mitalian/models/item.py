from django.db import models

from . import Collection

class Item(models.Model):
    name = models.CharField(max_length=256)
    label = models.CharField(max_length=256)
