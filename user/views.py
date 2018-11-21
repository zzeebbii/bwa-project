from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import request
from django.http import HttpResponse


# Create your views here.

def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid user name or password', extra_tags="danger")
            return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return HttpResponse("This is a profile page");