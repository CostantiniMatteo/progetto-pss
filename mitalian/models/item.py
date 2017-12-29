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
    votes_number = models.IntegerField()
    image = models.FilePathField(max_length=256)

    def add_vote(self, label):
        self.labels[label] += 1
        self.votes_number += 1

        maxs = [key for key in self.labels.keys()
                    if self.labels[key] == max(self.labels.values())]
        self.label = maxs[0] if len(maxs) == 1 else ''


    def is_valid_label(self, label):
        return label in self.collection.labels

    def __str__(self):
        return self.name
