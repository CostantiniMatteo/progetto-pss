from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Portebbe essere comodo salvarsi anche questo magari
    # progress = models.IngegerField()
