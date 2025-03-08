from django.urls import path
from .views import PostListView  # Import your view

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
]
