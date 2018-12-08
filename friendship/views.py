from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .models import Friendship
from django.shortcuts import render, redirect


@login_required
def find_friends(request):
    return render(request, 'findfriend.html')


def list_friends(request):
    if request.is_ajax():
        name = request.GET['name']
        friends = User.objects.filter(profile__real_name__icontains=name).exclude(pk=request.user.id)
        accepted = Friendship.objects.filter(req_from=request.user.id, is_accepted=True).values_list('req_to',
                                                                                                     flat=True)
        sent = Friendship.objects.filter(req_from=request.user.id, is_accepted=False).values_list('req_to', flat=True)
        html = render_to_string('friend_list.html', {'friends': friends, 'sent': sent, 'accepted': accepted})
        return HttpResponse(html)
    else:
        return HttpResponseForbidden("You are in a place where you should not be")


def friend_request(request):
    if request.is_ajax():
        request_to = request.POST['request_to']
        new_request = Friendship(req_from=request.user, req_to_id=request_to, is_accepted=False)
        new_request.save()

        return HttpResponse("{'status': true, 'message': 'Request Sent'}", content_type='application/json')
    else:
        return HttpResponseForbidden("You are in a place where you should not be")


def accept_request(request, id):
    friend_request = Friendship.objects.filter(id=id, req_to=request.user)
    if not friend_request:
        messages.error(request, 'You cannot accept this request', extra_tags="danger")
        return redirect('profile')
    else:
        friend_request.update(is_accepted=True)
        messages.error(request, 'Request accepted successfully', extra_tags="success")
        return redirect('profile')
