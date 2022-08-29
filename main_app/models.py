from django.db import models

# Create your models here.
class Podcast(models.Model):
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  hosts = models.TextField(max_length=250)
  rating = models.FloatField()