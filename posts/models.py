from django.db import models
from django.contrib.auth.models import User


def get_default_user():
    return User.objects.first().id  # Use the first user in the database


class Post(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, default=get_default_user)  # Set default
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title
