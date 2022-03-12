from django.http import HttpResponse

# CReate your views here
def welcome(request):
   return HttpResponse('Welcome to my app!')
