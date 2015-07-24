from django.shortcuts import render
from rest_framework.decorators import api_view

from authentication.models import User
from authentication.serializers import UserSerializer


from rest_framework.response import Response
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework import status

from rest_framework import permissions


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    res = {'res': 0, "msg": ""}

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            res['res'] = 1
            res['msg'] = "login success"
        else:
            res['res']= 0
            res['msg'] = "have not active"
    else:
        res['res'] = 0
        res['msg'] = "username or password is error"

    if res['res'] == 1:
        http_status = status.HTTP_200_OK
    else:
        http_status = status.HTTP_400_BAD_REQUEST
    return Response({"message": res['msg']}, http_status)


@api_view(('GET','POST'))
def logout(request):
    auth_logout(request)
    return Response("", status.HTTP_200_OK)




class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer