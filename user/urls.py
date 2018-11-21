from django.contrib import admin
from django.urls import path
from .views import profile
urlpatterns = [
    path(r'/profile', profile, name='profile')
]