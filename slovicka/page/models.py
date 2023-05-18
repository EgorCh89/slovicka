from django.db import models

# Create your models here.

class Dictionary(models.Model):
    name = models.TextField( default=None, unique=True)
    date = models.DateTimeField()
    creator_id = models.IntegerField(default=1)
    public = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.name}"

class Pair(models.Model):
    statement = models.TextField(max_length=64)
    definition = models.TextField(max_length=64)
    dict = models.ForeignKey(Dictionary, related_name="pairs", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.statement} = {self.definition}"
