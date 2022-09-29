from django.db import models

# Create your models here.
from django.forms import CharField

# Create your models here.
class Liked(models.Model):
    username=models.CharField(max_length=50)
    areaname=models.CharField(max_length=50)
    bhk=models.CharField(max_length=10)
    size=models.CharField(max_length=15)
    bathroom=models.CharField(max_length=10)
    duplex=models.CharField(max_length=5)
    parking=models.CharField(max_length=10)
    balcony=models.CharField(max_length=10)
    totalcost=models.CharField(max_length=25)
    def __str__(self):
      return str(self.username)
