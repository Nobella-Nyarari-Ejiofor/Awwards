from django.test import TestCase
from .models import Profile, Project,Ratings

# Create your tests here.

class ProfileTestClass(TestCase):
  
  def setUp(self):
    self.Nobella = Profile(user = 1, bio ="I love coding" , photo = "/profile/nobella.jpg" , contact="email:nobellanyarari@gmail.com")

  # testing instance

  def test_instance(self):
    self.assertTrue(isinstance(self.Nobella, Profile))

  #testing the save functionality
  def test_save_method(self):
    self.Nobella.profile.save()
    profile = Profile.objects.all()
    self.assertTrue(len(profile)>0)

  
  # test for getting an profile by user_id 
  def test_get_image(self):
    self.Nobella.save()
    profile_one = Profile.objects.filter(self.user_id)
    self.assertEqual(profile_one,self.photo)


class ProjectTestClass(TestCase):

   def setUp(self):
    self.Cafe = Project(title = "Cafe Jopo", image="project-url/image.jpg",description="An application for a reastraunt",link ="https:hontey.com",pub_date ="")


