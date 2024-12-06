from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task, Invitation
from .forms import TaskForm
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialAccount

def home(request):
    return render(request, 'base.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def register_view(request):
    """Handles user registration via an invitation token."""
    token = request.GET.get('token')  # Get the token from the query string
    invitation = Invitation.objects.filter(token=token, used=False).first()

    if not invitation:  # Check if the invitation is valid
        messages.error(request, "Invalid or expired invitation token.")
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the new user
            user.email = invitation.email  # Link user email to the invitation
            user.save()

            # Mark the invitation as used
            invitation.used = True
            invitation.save()

            messages.success(request, "Registration successful! You can now log in.")
            return redirect('account_login')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        # Delete social account data if needed
        SocialAccount.objects.filter(user=request.user).delete()
        logout(request)  # Log out the user
        request.session.flush()  # Clear the session
    return redirect('account_login')  # Redirect to login page after logout