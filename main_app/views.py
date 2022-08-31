from django.shortcuts import render, redirect
# Import create view
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Import model
from .models import Podcast, Guest
# Import EpisodeForm
from .forms import EpisodeForm


# Define views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def podcasts_index(request):
  podcasts = Podcast.objects.all()
  return render(request, 'podcasts/index.html', { 'podcasts': podcasts })

def podcasts_detail(request, podcast_id): # podcast_id is coming from urls.py (path('podcasts/<int:podcast_id>/...))
  podcast = Podcast.objects.get(id=podcast_id)
  # Get the guests the podcast doesn't have
  # id__in syntax is called a field lookup (get, exclude or filter)
  guests_podcast_doesnt_have = Guest.objects.exclude(id__in = podcast.guests.all().values_list('id'))
  # instantiate the episode form to be rendered in the template (creating an obkect from the class in forms.py)
  episode_form = EpisodeForm()
  return render(request, 'podcasts/detail.html', { 'podcast': podcast, 'episode_form': episode_form, 'guests': guests_podcast_doesnt_have })

def assoc_guest(request, podcast_id, guest_id):
  Podcast.objects.get(id=podcast_id).guests.add(guest_id) # ** Can pass a guest's id instead of the whole object!
  return redirect('detail', podcast_id=podcast_id)

def remove_guest(request, podcast_id, guest_id):
  Podcast.objects.get(id=podcast_id).guests.remove(guest_id)
  return redirect('detail', podcast_id=podcast_id)

def add_episode(request, podcast_id): # podcast_id is from urls.py in params for this function
  # Create a ModelForm instance using the data in request.POST
  form = EpisodeForm(request.POST)
  # Validate form
  if form.is_valid():
    new_episode = form.save(commit=False)
    # we are creating an object to save to the db, BUT don't save it yet bc we need to add podcast_id
    new_episode.podcast_id = podcast_id
    new_episode.save() # saves the feeding to the DB
  return redirect('detail', podcast_id=podcast_id) # diff bw this and render from podcasts_detail, is THIS is a *kwarg, the latter is a dict

class PodcastCreate(CreateView):
  model = Podcast
  fields = '__all__' # <- telling django what keys on the model we want to generate the form with 
  # ['title', 'genre', 'hosts', 'rating'] # if we dont want all of them, choose like this
  # redirect is the get_absolute_url defined in the model

class PodcastUpdate(UpdateView):
  model = Podcast
  # disallow renaming of podcast
  fields = ['genre', 'hosts', 'rating']

class PodcastDelete(DeleteView):
  model = Podcast
  success_url = '/podcasts/' # We define this, bc the get_absolute_url is going to the detail page, which wouldn't exist anymore

class GuestList(ListView):
  model = Guest

class GuestDetail(DetailView):
  model = Guest

class GuestCreate(CreateView):
  model = Guest
  fields = '__all__'

class GuestUpdate(UpdateView):
  model = Guest
  fields = ['name', 'occupation']

class GuestDelete(DeleteView):
  model = Guest
  success_url = '/guests/'