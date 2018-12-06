from django.urls import path, re_path
from . import views
urlpatterns = [
    path(r'', views.show_discussions, name="discussion_list"),
    path(r'create', views.create_discussion, name="create_discussion"),
    path(r'view/<int:id>', views.view_discussion, name='view_discussion'),
    path(r'comments/<int:id>', views.load_comments , name='comment_list'),
    path(r'comment/create', views.new_comment ,name='new_comment'),
]