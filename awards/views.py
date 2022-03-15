from django.contrib import messages
from django.db import transaction
from django.shortcuts import render , redirect
from .forms import UploadProjectForm, CreateProfileForm
from django.contrib.auth.decorators import login_required
from awards.models import Project , Profile


# CReate your views here

@login_required(login_url='/accounts/login/')
def index(request):

  project = Project.objects.all().order_by('-id')
  current_user=request.user
  user_profile= Profile.objects.filter(id=current_user.id)
  
  # note we use request.user.profile as the profile has a one to one relationship with the user
  current_user = request.user.profile

  # For the upload project model
  if request.method == 'POST':
    upload_project =UploadProjectForm(request.POST, request.FILES)

    if upload_project.is_valid():
      project = upload_project.save(commit=False)
      project.user = current_user
      project.save()

    return redirect('index')

  else:
    upload_project = UploadProjectForm()

   

  return render (request , 'awards/index.html',{"projects":project , "form":upload_project , "profile":user_profile})

def search_results(request):
  if 'project' in request.GET and request.GET["project"]:
    search_term=request.GET.get("project")
    searched_projects=Project.search_by_title(search_term)

    message=f"{search_term}"
    return render(request,'awards/search.html',{"message":message , "projects":searched_projects})
  
  else:
    message="You haven't searched for any term"
    return render (request,'awards/search.html',{"message":message})



@transaction.atomic
@login_required(login_url='/accounts/login')
def profile(request):
  current_user= request.user.profile
  user_profile= Profile.objects.filter(id=current_user.id)
  users_projects = Project.objects.filter(user_id = current_user.id).all()
  

  if request.method == 'POST':
    create_profile =CreateProfileForm(request.POST,request.FILES, instance = request.user.profile)

    if create_profile.is_valid():
      user_profile = create_profile.save(commit=False)
      user_profile.save()
    
      messages.success(request,('Your profile was successfully updated!'))
      return redirect('profile')

    else:
      messages.error(request,"please correct the error below")

  else:
     create_profile= CreateProfileForm(instance= request.user.profile)
  return render(request , 'awards/profile.html', {"profile":user_profile,"projects":users_projects, "form":create_profile })