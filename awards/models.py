from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):

  """
  A model that contains a user profile and it's details
  """
  user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile', null=True)
  name = models.CharField(max_length=50)
  bio=models.TextField(max_length=500 , blank=True)
  photo=models.ImageField(upload_to="profile/")
  contact=models.CharField(max_length = 50)

  def __str__(self):
    return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Project(models.Model):
  """
  A model on the projects 
  """
  title= models.CharField(max_length=50)
  image=models.ImageField(upload_to="project-images/")
  description =models.TextField(max_length= 500)
  link=models.CharField(max_length=200)
  user= models.ForeignKey(Profile, on_delete= models.CASCADE,related_name='projects', null=True)
  pub_date = models.DateTimeField(auto_now_add=True)

  
  def __str__(self):
    return f'{self.title}'

  @classmethod
  def search_by_title(cls,search_term):
    project_searched=cls.objects.filter(title__icontains=search_term)
    return project_searched