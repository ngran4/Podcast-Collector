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
  path('podcasts/<int:podcast_id>/add_episode/', views.add_episode, name='add_episode'),
  # Associate a guest with a podcast (M:M)
  path('podcasts/<int:podcast_id>/assoc_guest/<int:guest_id>/', views.assoc_guest, name='assoc_guest'),
  path('guests/', views.GuestList.as_view(), name='guests_index'),
  path('guests/<int:pk>/', views.GuestDetail.as_view(), name='guests_detail'),
  path('guests/create/', views.GuestCreate.as_view(), name='guests_create'),
  path('guests/<int:pk>/update/', views.GuestUpdate.as_view(), name='guests_update'),
  path('guests/<int:pk>/delete/', views.GuestDelete.as_view(), name='guests_delete'),
]