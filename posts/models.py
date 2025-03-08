from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile  # Ensure this is correct


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
