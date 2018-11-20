from django.db import models
from django.contrib.auth.models import User

# Model for storing user info
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.DateField(null=True)
    country=models.TextField(max_length=100, blank=True)
    city=models.TextField(max_length=100, blank=True)
    phone=models.TextField(max_length=20, blank=True)
