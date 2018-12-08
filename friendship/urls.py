from django.contrib import admin
from django.urls import path
from friendship import views


urlpatterns = [
    path(r'', views.find_friends, name='friends_default'),
    path(r'find', views.find_friends, name='find_friends'),
    path(r'list', views.list_friends, name='list_friends'),
    path(r'newrequest', views.friend_request, name='new_request'),
    path(r'accept/<int:id>', views.accept_request, name='accept_request'),

]