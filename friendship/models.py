from django.contrib.auth.models import User
from django.db import models


class Friendship(models.Model):
    req_from = models.ForeignKey(User, related_name='req_from', on_delete=models.CASCADE)
    req_to = models.ForeignKey(User, related_name='req_to', on_delete=models.CASCADE)
    is_accepted = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)