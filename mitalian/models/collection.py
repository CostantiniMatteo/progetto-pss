from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Collection(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # labeled images / total images
    progress = models.IntegerField()
    # Allowed labels for collection's images
    labels = ArrayField(models.CharField(max_length=256))
    # Where you can label images of this collection
    link = models.URLField()
    # Password required to labels images of this collection
    password = models.TextField()

    def __str__(self):
        return self.name
