from django.db import models
from django.urls import reverse

# Create your models here.

class Guest(models.Model):
  name = models.CharField(max_length=75)
  occupation = models.CharField(max_length=75)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('guests_detail', kwargs={'pk': self.id})  

class Podcast(models.Model): # <- inheriting from models.Model class, gives our class the power/methods to talk to DB
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  hosts = models.TextField(max_length=250)
  rating = models.FloatField()
  # Add the M:M relationship
  guests = models.ManyToManyField(Guest)

  # this function will get called on a create or update on a Class Based View in order to redirect the user
  def get_absolute_url(self):
    # reverse will return the correct path for the detail named route
    # since that route requires a cat_id route parameter, its value must be provided here
    return reverse('detail', kwargs={'podcast_id': self.id})


class Episode(models.Model):
  date = models.DateField('Release Date')
  episode = models.CharField(max_length=150)

  # create the podcast_id FK
  # on_delete ensures that if a Podcast is deleted, all Episodes will also be deleted (so no episodes exist w/o the pod)
  podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.episode} released on {self.date}"
  
  # Changing the default sort (to descending--eg most recent)
  class Meta:
    ordering = ['-date'] # '-date' gives descending order, 'date' would be ascending