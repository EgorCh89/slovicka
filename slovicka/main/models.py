from django.db import models

# Create your models here.
class Pair(models.Model):
    statement = models.TextField(max_length=64)
    definition = models.TextField(max_length=64)

class Dictionary(models.Model):
    pairs = models.ManyToManyField(Pair, related_name="pairs")
