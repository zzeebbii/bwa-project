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
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    req_from=models.IntegerField()
    req_to=models.IntegerField()
    is_accepted=models.SmallIntegerField()
    datetime=models.DateTimeField()

class Status(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status_text=models.TextField()
    status_time=models.DateTimeField()
    is_public=models.BooleanField()
    likes=models.TextField()

class Comments(models.Model):
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    comment_text=models.TextField()
    comment_by=models.IntegerField()
    datetime=models.DateTimeField()
