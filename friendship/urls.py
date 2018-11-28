from django.contrib import admin
from django.urls import path
from friendship import views


urlpatterns = [
    path(r'sendrequest', views.find_friend, name='findfriend'),
]
