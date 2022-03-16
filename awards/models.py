from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Profile(models.Model):

  """
  A model that contains a user profile and it's details
  """
  user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile', null=True)
  bio=models.TextField(max_length=500 , blank=True,null=True)
  photo=models.ImageField(upload_to="profile/" , blank=True)
  contact=models.CharField(max_length = 50, blank=True ,null= True)

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
  image=models.ImageField(upload_to="project-images/", null =True)
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

class Ratings(models.Model):
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  project= models.ForeignKey(Project, on_delete=models.CASCADE)
  design = models.IntegerField(choices=list(zip(range(1,10), range(1,10))), unique=True)
  usability = models.IntegerField(choices=list(zip(range(1,10), range(1,10))), unique=True)
  content = models.IntegerField(choices=list(zip(range(1,10), range(1,10))), unique=True)
  average=models.FloatField(validators= [MinValueValidator(0,0), MaxValueValidator(10,0)], default=0)


