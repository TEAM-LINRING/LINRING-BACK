from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.shortcuts import render, redirect

# Create your views here.
@api_view(['DELETE'])
def userDelete(request, id):
    try:
        uid = User.objects.get(id=id)
        # user1 = authenticate(request, email="test1@example.com", password="1q2w3e4r!@")
        user1 = authenticate(request, email="admin@example.com", password="1234")
        login(request, user1)
        print(type(user1))
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        print("request user : " + request.user.email)
        print("uid user : " + uid.email)
        if request.user.is_staff:
            pass
        elif request.user.id == id:
            logout(request)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        uid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

