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
from authentication.permissions import IsUserOwner
from authentication.permissions import IsAdmin


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
    return Response({"message": "logout success"}, status.HTTP_200_OK)

class BaseModelView(viewsets.ModelViewSet):
    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """

        u = IsAdmin()

        if u.has_permission(request,self):
            return True

        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                self.permission_denied(request)

    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        u = IsAdmin()
        if u.has_object_permission(request,self,obj):
            return True
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                self.permission_denied(request)


class UserViewSet(BaseModelView):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.AllowAny(), )
        elif self.request.method == 'GET':
            if self.action == 'list':
                return (IsAdmin(), )
            elif self.action == 'retrieve':
                return (IsUserOwner(),)
        return (IsAdmin(), )

    def create(self, request, *args, **kwargs):
        try:
            username = request.DATA['username']
            password = request.DATA['password']
            User.objects.create_user(username, password)
            return Response(request.DATA, status.HTTP_200_OK)
        except:
            return Response({"message":"can not register user using received data"},
                            status.HTTP_400_BAD_REQUEST)