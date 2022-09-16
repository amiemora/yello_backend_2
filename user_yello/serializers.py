from rest_framework import serializers 
from .models import Post
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')

    def create(self, validated_data):
        user = User.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self,instance, validated_data):
        user = User.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user


class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post 
        fields = ('author', 'title', 'image', 'description', 'likes')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('post','commenter_name','comment_body', 'likes')


