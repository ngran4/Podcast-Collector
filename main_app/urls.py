from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('podcasts/', views.podcasts_index, name="index"),
  path('podcasts/<int:podcast_id>/', views.podcasts_detail, name='detail'),
]