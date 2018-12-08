from django.contrib import admin
from friendship.models import Friendship


# Register your models here.


# Register your models here.
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['req_from', 'req_to', 'is_accepted', 'created_at', 'updated_at']


admin.site.register(Friendship, FriendshipAdmin)