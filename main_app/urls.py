from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('podcasts/', views.podcasts_index, name="index"),
  path('podcasts/<int:podcast_id>/', views.podcasts_detail, name='detail'),
  path('podcasts/create/', views.PodcastCreate.as_view(), name='podcasts_create'),
  # pk (primary key, aka the cat_id) is what the django views is expecting as a param if we need one 
  path('podcasts/<int:pk>/update/', views.PodcastUpdate.as_view(), name='podcasts_update'),
  path('podcasts/<int:pk>/delete/', views.PodcastDelete.as_view(), name='podcasts_delete'),
  path('podcasts/<int:podcast_id>/add_episode/', views.add_episode, name='add_episode')
]