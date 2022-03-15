from rest_framework import serializers
from.models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model =Profile
    fields =('user', 'bio','photo','contact')

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title','image','description','link','user','pub_date')