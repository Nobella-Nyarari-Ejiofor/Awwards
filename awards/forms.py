from django.contrib.auth.models import User
from  django import forms
from .models import Profile, Project

class UploadProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude =['user']

class CreateProfileForm(forms.ModelForm):
  class Meta:
    model=Profile
    exclude =['user']

class RatingsForm(forms.ModelChoiceField):
  class Meta:
    model ="Ratings"
    exclude = ['user','project']

