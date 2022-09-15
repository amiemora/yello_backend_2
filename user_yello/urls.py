from django.urls import path
from . import views 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/users/login', csrf_exempt(views.check_login), name="check_login"),
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/post', views.PostList.as_view(), name='post'),
    path('api/post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
]