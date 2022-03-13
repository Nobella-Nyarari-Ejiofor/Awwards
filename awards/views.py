from django.shortcuts import render

# CReate your views here
def index(request):
  return render (request , 'awards/index.html')