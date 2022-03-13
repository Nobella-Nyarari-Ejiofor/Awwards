from django.contrib import admin
from django.forms import models
from .models import Profile, Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
