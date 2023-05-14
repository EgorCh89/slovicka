from django.db import models

# Create your models here.
class Pair(models.Model):
    statement = models.TextField(max_length=64)
    definition = models.TextField(max_length=64)
    
    def __str__(self):
        return f"{self.statement} : {self.definition}"



class Dictionary(models.Model):
    name = models.TextField( default=None)
    pairs = models.ManyToManyField(Pair, related_name="pairs")
    def __str__(self) -> str:
        return f"{self.name}"