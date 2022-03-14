from django.urls import path , re_path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns=[
path('',views.index , name='index'),
re_path(r'^search/', views.search_results, name='search_results'),
re_path(r'^profile/', views.profile, name="profile"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)