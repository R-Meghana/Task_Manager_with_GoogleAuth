from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string  # For generating unique tokens

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Define a top-level function for generating the token
def generate_unique_token():
    return get_random_string(64)


class Invitation(models.Model):
    email = models.EmailField(unique=True)  # The invited user's email
    token = models.CharField(
        max_length=64,
        unique=True,
        default=generate_unique_token  # Use the top-level function
    )
    invited_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the invitation
    used = models.BooleanField(default=False)  # To track whether the invitation has been used

    def __str__(self):
        return self.email
