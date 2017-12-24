from django.db import models
from django.contrib.postgres.fields import JSONField

from . import Collection

class Item(models.Model):
    name = models.CharField(max_length=256)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    label = models.CharField(max_length=256)
    # { 'label1': n_votes, 'label2': n_votes, ... }
    labels = JSONField()
    last_feched = models.DateTimeField(null=True, blank=True)
    image = models.FilePathField(max_length=256)

    def __str__(self):
        return self.name
