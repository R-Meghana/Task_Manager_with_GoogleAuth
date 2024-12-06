from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('tasks/', include('tasks.urls')),
    path('register/', lambda request: redirect('/tasks/register/' + (f"?{request.META['QUERY_STRING']}" if request.META['QUERY_STRING'] else ''))),
]
