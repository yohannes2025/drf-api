# posts/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from profiles.serializers import ProfileSerializer

from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter'
        ]
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
