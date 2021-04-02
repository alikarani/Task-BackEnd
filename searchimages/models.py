from django.db import models

# Create your models here.
# application/models.py
from django.db import models

class FavouriteImage(models.Model):
    imageUrl = models.CharField(max_length=100)

class list1(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)