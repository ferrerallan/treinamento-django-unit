from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=100)
    canFly = models.BooleanField()
    genre = models.CharField(max_length=10)
