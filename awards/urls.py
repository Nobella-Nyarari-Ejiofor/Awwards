from django.urls import path , re_path
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns=[
path('',views.index , name='index'),
re_path(r'^search/', views.search_results, name='search_results'),
re_path(r'^profile/', views.profile, name="profile"),
re_path(r'^api/profile/$', views.ProfileList.as_view()),
re_path(r'^api/project/$', views.ProjectList.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)