from django.db import models
from django.contrib.auth.models import User

# Model for storing user info
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.DateField(null=True)
    country=models.TextField(max_length=100, blank=True)
    city=models.TextField(max_length=100, blank=True)
    phone=models.TextField(max_length=20, blank=True)

class Friendship(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    req_from=models.PositiveIntegerField()
    req_to=models.PositiveIntegerField()
    is_accepted=models.PositiveSmallIntegerField()
    datetime=models.DateTimeField(auto_now_add=True, blank=True)

class Status(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    status_text=models.TextField()
    status_time=models.DateTimeField(auto_now_add=True, blank=True)
    is_public=models.BooleanField(default=True)
    likes=models.PositiveIntegerField(default=0)

class Comments(models.Model):
    status=models.OneToOneField(Status, on_delete=models.CASCADE)
    comment_text=models.TextField()
    comment_by=models.PositiveIntegerField()
    datetime=models.DateTimeField(auto_now_add=True, blank=True)
