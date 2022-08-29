from django.shortcuts import render
from .models import Podcast

from django.http import HttpResponse

# podcasts = [
#   Podcast('Pod Save America', 'Politics', 'Dan Pfeiffer, Jon Favreau, Jon Lovett, Tommy Vietor', 4.5),
#   Podcast('RedHanded', 'True Crime', 'Hannah Maguire, Suruthi Bala', 4.7),
#   Podcast('Girls Gotta Eat', 'Comedy', 'Ashley Hesseltine, Rayna Greenburg', 4.7),
#   Podcast('Gola', 'Food & Culture', 'Katie Parla, Danielle Callegari', 4.9),
#   Podcast('Conflicted', 'History', 'Aimen Dean, Thomas Small', 4.8)
# ]


# Define views
def home(request):
  return HttpResponse('<h1>yoohoo</h1>')

def about(request):
  return render(request, 'about.html')

def podcasts_index(request):
  podcasts = Podcast.objects.all()
  return render(request, 'podcasts/index.html', { 'podcasts': podcasts })

def podcasts_detail(request, podcast_id):
  podcast = Podcast.objects.get(id=podcast_id)
  return render(request, 'podcasts/detail.html', { 'podcast': podcast })