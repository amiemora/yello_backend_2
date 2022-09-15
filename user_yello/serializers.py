from rest_framework import serializers 
from .models import Post
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')


class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post 
        fields = ('id','author', 'title', 'iamge', 'description',)