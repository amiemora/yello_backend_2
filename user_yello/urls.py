

from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('post', views.PostList.as_view(), name='post'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
]
