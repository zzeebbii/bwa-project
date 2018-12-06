from django.contrib import admin
from django.urls import path
from friendship import views


urlpatterns = [
    path(r'find', views.find_friends, name='find_friends'),
    path(r'list', views.list_friends, name='list_friends'),

]