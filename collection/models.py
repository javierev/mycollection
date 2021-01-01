from django.db import models

# Create your models here.

class Console(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)

class Game(models.Model):
    console = models.ForeignKey(Console, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
