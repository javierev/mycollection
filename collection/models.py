from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    iso_code = models.CharField(max_length=2)

class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)

class Console(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    year = models.IntegerField(default=1999)
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name + ' (' + self.short_name + ')'

class Game(models.Model):
    console = models.ForeignKey(Console, on_delete=models.RESTRICT)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
