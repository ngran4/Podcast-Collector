from django.forms import ModelForm # gives us the power to generate form from model and save to database
from .models import Episode


class EpisodeForm(ModelForm):
  class Meta: # meta class ~ description about the class (configuration options)?
    model = Episode
    fields = ['date', 'episode']