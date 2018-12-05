from django.db import models
from django.contrib.auth.models import User

class Discussions(models.Model):
    topic = models.CharField(max_length=255, default='')
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = [models.F('created_at').desc()]


class DiscussionComments(models.Model):
    discussion_id = models.ForeignKey(Discussions, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
