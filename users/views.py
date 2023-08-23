from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def userDelete(request):
    if request.user.is_authenticated:
        user = request.user
        print(user.email)
        user.delete()
        logout(request)
    context = {}
    return render(request, 'users/delete_success.html', context)
