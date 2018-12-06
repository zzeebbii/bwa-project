import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from . import forms
from .models import Discussions, DiscussionComments
from django.template.loader import render_to_string


# Create your views here.
def show_discussions(request):
    discussions = Discussions.objects.all()
    return render(request, 'discussions.html', { 'discussions' : discussions})


def create_discussion(request): 
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.DiscussionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            topic = form.cleaned_data['topic']
            discussion_text = form.cleaned_data['text']
            discussion = Discussions(topic=topic, text=discussion_text, created_by=request.user)
            discussion.save()
            return HttpResponseRedirect(reverse('discussion_list'))



    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.DiscussionForm()

    return render(request, 'create.html', {'form': form})


def view_discussion(request, id = 1):
    discussion = Discussions.objects.get(pk=id)
    return render(request, 'view.html', {'discussion' : discussion})


def load_comments(request, id = 1):
    comments = DiscussionComments.objects.filter(discussion_id=id);
    html = render_to_string('comments.html', {'comments' : comments})
    return HttpResponse(html)


def new_comment(request):
    if request.is_ajax():
        comment = request.POST['comment']
        discussion = request.POST['discussion']
        comment_object = DiscussionComments(text=comment, discussion_id=Discussions.objects.get(pk=discussion)
                                            ,comment_by_id=request.user.id)
        comment_object.save()
        return HttpResponse(json.dumps({"status" : True, "message": 'Saved successfully'}), content_type="application/json")
    else:
        return Http404("No resource found")