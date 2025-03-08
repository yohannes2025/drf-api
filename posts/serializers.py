# posts/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from profiles.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        """
        Returns True if the current user is the owner of the post, False otherwise.
        """
        request = self.context['request']
        return obj.owner == request.user

    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'updated_at', 'title',
                  'content', 'image', 'is_owner', 'profile_id', 'profile_image']
        read_only_fields = ['id', 'created_at', 'updated_at',
                            'owner', 'is_owner', 'profile_id', 'profile_image']
