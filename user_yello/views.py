from django.shortcuts import render, redirect
from .serializers import UserSerializer, PostSerializer
from rest_framework import generics
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import User, Group 
from .models import Post
from django.http import JsonResponse
import json
from django.views import generic

from user_yello import serializers

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer

class PostDetail(generic.DetailView):
    model = Post 
    serializer_class = PostSerializer



def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) 
        username = jsonRequest['username'] 
        password = jsonRequest['password'] 
        if User.objects.get(username=username): 
            user = User.objects.get(username=username)  
            if check_password(password, user.password): 
                return JsonResponse({'id': user.id, 'username': user.username}) #if passwords match, return a user dict
            else: #passwords don't match so return empty dict
                return JsonResponse({})
        else: #if email doesn't exist in db, return empty dict
            return JsonResponse({})
  

