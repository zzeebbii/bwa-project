from django.contrib import admin
from user.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.get_fields()]


admin.site.register(Profile, ProfileAdmin)