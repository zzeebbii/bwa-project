from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.http import request
from django.http import HttpResponse

# Create your views here.


def find_friend(request):
    return render(request, 'findfriend.html')
