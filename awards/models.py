from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):

  """
  A model that contains a user profile and it's details
  """
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  bio=models.TextField(max_length=500 , blank=True)
  photo=models.ImageField(upload_to="profile/")
  contact=models.CharField(max_length = 50)

  def __str__(self):
    return f'{self.user.username}'


class Project(models.Model):
  """
  A model on the projects 
  """
  title= models.CharField(max_length=50)
  image=models.ImageField(upload_to="project-images/")
  description =models.TextField(max_length= 500)
  link=models.CharField(max_length=200)
  projects= models.ForeignKey(Profile, on_delete= models.CASCADE)

  
  def __str__(self):
    return f'{self.title}'
