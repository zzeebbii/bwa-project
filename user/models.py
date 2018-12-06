from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='images/')
    real_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    email_confirmed = models.BooleanField(default=False)
    dob = models.DateField(null=True)
    country = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    print("Triggered")
    if created:
        Profile.objects.get_or_create(user=instance)
    instance.profile.save()


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_text = models.TextField()
    status_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_public = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(default=0)


class Comments(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_by = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
