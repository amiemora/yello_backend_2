import datetime
from django.shortcuts import render, redirect
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from rest_framework import generics
from .forms import RegisterForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import User, Group
from .models import Post, Comment
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json
from . import views
from rest_framework import serializers 
from django.forms.models import model_to_dict
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('author')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('author')
    serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('post')
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().order_by('post')
    serializer_class = CommentSerializer


def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':

        jsonRequest = json.loads(request.body) #make the request JSON format
        username = jsonRequest['username'] #get the username from the request
        password = jsonRequest['password'] #get the password from the request
        if User.objects.get(username=username): #see if username exists in db
            user = User.objects.get(username=username)  #find user object with matching username
            if check_password(password, user.password): #check if passwords match
                return JsonResponse({'id': user.id, 'username': user.username}) #if passwords match, return a user dict
            else: #passwords don't match so return empty dict
                return JsonResponse({})
        else: #if username doesn't exist in db, return empty dict
            return JsonResponse({})



# @login_required(login_url="/login")
# def home (request):
#     posts = Post.objects.all()

#     if request.method == "POST":
#         post_id = request.POST.get("post-id")
#         user_id = request.POST.get("user-id")

#         if post_id: 
#             post = Post.objects.filter(id = post_id).first()
#             if post and (post.author == request.user or request.user.has_perm("user_yello.delete_post")):
#                 post.delete()
#         elif user_id: 
#             user = User.objects.filter(id=user_id).first()
#             if user and request.user.is_staff:
#                 try:
#                     group = Group.objects.get(name='default')
#                     group.user_set.remove(user)
#                 except: 
#                     pass
#                 try: 
#                     group = Group.objects.get(name='mod')
#                     group.user_set.remove(user)
#                 except:
#                     pass    
                         
#     return render(request, 'user_yello/home.html', {"posts": posts})

# @login_required(login_url="/login")
# @permission_required("user_yello.add_post", login_url="/login", raise_exception=True) 
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('/home')
#     else: 
#         form = PostForm()

#     return render(request, 'user_yello/create_post.html', {"form": form})

# def sign_up(request):
#     if request.method == 'POST':
#             form  = RegisterForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login(request, user)
#                 return redirect ('/home')
#     else: 
#             form = RegisterForm()

#     return render (request, 'registration/sign_up.html', {"form": form})


# def add_comment(request, pk):
#     eachPost = Post.objects.get(id=pk)

#     form = CommentForm(instance=eachPost)

#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=eachPost)
#         if form.is_valid():
#             name = request.user.username
#             body = form.cleaned_data["comment_body"]
#             c = Comment(product=eachPost, commenter_name=name, comment_body=body, created_at=datetime.now())
#             c.save()
#             return redirect('/home')
#         else:
#             print('form is invalid')
#     else: 
#         form = CommentForm()


#     context = {'form': form}

#     return render()

# import Comment & CommentForm
