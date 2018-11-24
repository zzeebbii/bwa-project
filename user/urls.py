from django.contrib import admin
from django.urls import path
from .views import profile
from .views import signup
urlpatterns = [
    path(r'profile', profile, name='profile'),
    path(r'signup', signup, name='signup')
]
