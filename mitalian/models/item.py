from django.db import models
from django.contrib.postgres.fields import JSONField

from . import Collection

class Item(models.Model):
    name = models.CharField(max_length=256)
    label = models.CharField(max_length=256)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    # { 'label1': n_votes, 'label2': n_votes, ... }
    labels = JSONField()

    def __str__(self):
        return self.name
