from django.db import models

# Create your models here.
# application/models.py
from django.db import models

class FavouriteImage(models.Model):
    imageUrl = models.CharField(max_length=100)