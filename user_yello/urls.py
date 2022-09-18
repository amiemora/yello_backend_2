

from django.urls import path
from . import views 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/post', views.PostList.as_view(), name='post'),
    path('api/post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('api/users/login', csrf_exempt(views.check_login), name="check_login"),
    path('api/comments',views.CommentList.as_view(), name='comment_list'),
    path('api/comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]



#  path('post/<int:pk>/add-comment', views.add_comment, name='add_comment'),

   
