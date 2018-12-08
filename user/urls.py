from django.contrib import admin
from django.urls import path
from .views import profile, edit_profile, profile_info, delete_account
from .views import signup

urlpatterns = [
    path(r'profile', profile, name='profile'),
    path(r'signup', signup, name='signup'),
    path(r'profile/edit', edit_profile, name='editprofile'),
    path(r'profile/info/<int:id>', profile_info, name='profileinfo'),
    path(r'delete', delete_account, name='delete_account'),
]
