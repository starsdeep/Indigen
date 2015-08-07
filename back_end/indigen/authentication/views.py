from django.shortcuts import render
from rest_framework.decorators import api_view
import sys
from location.models import Country
from authentication.models import User, Local
from authentication.serializers import UserSerializer
from authentication.forms import RegisterModel
from rest_framework.response import Response
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from authentication.permissions import IsUserOwner
from authentication.permissions import IsAdmin
from django.forms.forms import ValidationError
from base_class.views import BaseModelView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from filesystem.models import Image
from base_class import functions

@api_view(('POST', ) )
def login(request):

    try:
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
    except:
        return Response({"message":"can not login using retrieve data"}, status.HTTP_400_BAD_REQUEST)

    result = False
    msg = ""

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            result = True
            serializer = UserSerializer(request.user)
            user_data = serializer.data
            token, created = Token.objects.get_or_create(user=user)
            user_data['token'] = token.key
            return Response(user_data, status.HTTP_200_OK)
        else:
            result = False
            msg = "have not active"
    else:
        result = False
        msg = "username or password is error"

    if result:
        http_status = status.HTTP_200_OK
    else:
        http_status = status.HTTP_400_BAD_REQUEST

    return Response({"message": msg}, http_status)


@api_view(('GET','POST'))
def logout(request):
    auth_logout(request)
    return Response({"message": "logout success"}, status.HTTP_200_OK)


@api_view(('PUT',))
def password_update(request):
    if not request.user.is_anonymous():
        errors = {}
        try:
            try:
                old_password = request.DATA['old_password']
            except:
                errors['old_password'] = ["old_password can not be blank", ]

            try:
                new_password = request.DATA['new_password']
                assert new_password != ""
            except:
                errors['new_password'] = ["new_password can not be blank", ]


            if request.user.check_password(old_password):
                request.user.set_password(new_password)
                request.user.save()
                return Response({"message":"update success"}, status.HTTP_200_OK)
            else:
                if errors.has_key('old_password'):
                    errors['old_password'].append("old_password is not correct")
                else:
                    errors['old_password'] = ["old_password is not correct", ]
        except:
            return Response({"message":"can not update password","errors":errors}, status.HTTP_400_BAD_REQUEST)
        return Response({"message":"can not update password","errors":errors}, status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"message": "you should login first"}, status.HTTP_401_UNAUTHORIZED)



class Profile(APIView):
    """
    get profile
    update profile
    """

    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({"message":"can not access your profile, login first"}, status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        user = request.user
        try:
            user.age = request.DATA['age']
        except:
            pass

        try:
            user.local.service_introduction = request.DATA['service_introduction']
            user.local.save()
        except:
            local = Local(user=user)
            local.service_introduction = request.DATA['service_introduction']
            local.save()

        try:
            user.is_male = request.DATA['is_male']
        except:
            pass

        try:
            user.save()
            u = UserSerializer(request.user)
            return Response(u.data, status.HTTP_200_OK)
        except:
            return Response({"message": "internal error, fail to update profile"}, status.HTTP_400_BAD_REQUEST)



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
            data = request.DATA
            errors = {}
            try:
                r = RegisterModel(**data)
                r.full_clean()
            except ValidationError, e:
                errors = e.message_dict
            except:
                print "Unexpected error:", sys.exc_info()[0]

            if len(errors) == 0:
                try:
                    User.objects.create_user(username=r.telephone, password=r.password, country=r.country, nickname=r.nickname)
                    return Response(request.DATA, status.HTTP_200_OK)
                except:
                    print "unexcepted error:", sys.exc_info()[0]
                    return Response({"message":"can not register, internal error"},
                            status.HTTP_400_BAD_REQUEST)
            else:


                return Response(
                        {
                            "message": "can not register user using received data",
                            "errors": errors,
                        },
                        status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message":"can not register user using received data"},
                            status.HTTP_400_BAD_REQUEST)