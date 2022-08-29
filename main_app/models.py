from django.db import models
from django.urls import reverse

# Create your models here.
class Podcast(models.Model): # <- inheriting from models.Model class, gives our class the power/methods to talk to DB
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  hosts = models.TextField(max_length=250)
  rating = models.FloatField()

  # this function will get called on a create or update on a Class Based View in order to redirect the user
  def get_absolute_url(self):
        # reverse will return the correct path for the detail named route
    # since that route requires a cat_id route parameter, its value must be provided here
    return reverse('detail', kwargs={'podcast_id': self.id})