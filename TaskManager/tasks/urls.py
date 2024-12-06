from django.urls import path
from . import views

# app_name = 'tasks'

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Default page for tasks
    path('create/', views.task_create, name='task_create'),  # Create new task
    path('edit/<int:id>/', views.task_edit, name='task_edit'),  # Edit task
    path('delete/<int:id>/', views.task_delete, name='task_delete'),  # Delete task
    path('register/', views.register_view, name='register'), # Register route
    path('logout/', views.logout_view, name='logout'),
    # path('google/login/', views.custom_google_login_view, name='google_login'),
]
