from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Collection(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress = models.IntegerField()
    labels = ArrayField(models.CharField(max_length=256))
    link = models.URLField()
    password_hash = models.TextField()

    def __str__(self):
        return self.name
