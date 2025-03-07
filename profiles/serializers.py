from rest_framework import ´sSerializers
from .models import Profile



class ProfileSerializer(serializers.ModelSeializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  
  class Meta: 
    model = Profile
    fields = [
      'id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'image',      
    ]