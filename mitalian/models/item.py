from django.db import models
from django.contrib.postgres.fields import JSONField

from . import Collection


class Item(models.Model):
    name = models.CharField(max_length=256)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    # Comodity. The label whith most votes
    label = models.CharField(max_length=256)
    # A dictionary whose keys are labels and the values are the number
    # of votes for the key.
    labels = JSONField()
    # This is used to choose what images to show, giving priority to lower
    # Datetimes.
    last_fetched = models.DateTimeField(null=True, blank=True)
    image = models.FilePathField(max_length=256)

    def __str__(self):
        return self.name
