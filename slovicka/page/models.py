from django.db import models

# Create your models here.
class Pair(models.Model):
    statement = models.TextField(max_length=64)
    definition = models.TextField(max_length=64)
    
    def __str__(self):
        return f"{self.statement} = {self.definition}"



class Dictionary(models.Model):
    name = models.TextField( default=None)
    pairs = models.ManyToManyField(Pair, related_name="pairs")
    date = models.DateTimeField()
    creator_id = models.IntegerField()
    public = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.name}"