from email import message
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from awards.models import Project

# CReate your views here
# @login_required(login_url='/accounts/login/')
def index(request):
  return render (request , 'awards/index.html')

def search_results(request):
  if 'project' in request.GET and request.GET["project"]:
    search_term=request.GET.get("project")
    searched_projects=Project.search_by_title(search_term)

    message=f"{search_term}"
    return render(request,'awards/search.html',{"message":message , "projects":searched_projects})
  
  else:
    message="You haven't searched for any term"
    return render (request,'awards/search.html',{"message":message})