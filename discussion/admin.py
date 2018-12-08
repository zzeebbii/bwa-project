from django.contrib import admin
from discussion.models import Discussions, DiscussionComments


# Register your models here.


# Register your models here.
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ['topic', 'text', 'created_by', 'created_at', 'updated_at']


class DiscussionCommentAdmin(admin.ModelAdmin):
    list_display = ['discussion_id', 'text', 'created_at']


admin.site.register(Discussions, DiscussionAdmin)
admin.site.register(DiscussionComments, DiscussionCommentAdmin)
