from django.contrib import admin

# import models
from .models import Podcast, Episode

# Register your models here.
admin.site.register(Podcast)
admin.site.register(Episode)