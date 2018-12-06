from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.template.loader import render_to_string


@login_required
def find_friends(request):
    return render(request, 'findfriend.html')


def list_friends(request):
    if request.is_ajax():
        name = request.GET['name']
        friends = User.objects.filter(profile__real_name__contains=name)
        html = render_to_string('friend_list.html', {'friends': friends})
        return HttpResponse(html)
    else:
        return HttpResponseForbidden("You are in a place where you should not be")
