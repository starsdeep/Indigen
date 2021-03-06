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
from location.models import City
import json



from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings

from rest_framework_jwt.serializers import (
    JSONWebTokenSerializer, RefreshJSONWebTokenSerializer,
    VerifyJSONWebTokenSerializer
)

from rest_framework_jwt.utils import jwt_payload_handler

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class JSONWebTokenAPIView(APIView):
    """
    Base API View that various JWT interactions inherit from.
    """
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'view': self,
        }

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__)
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)

            return Response(response_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer


class VerifyJSONWebToken(JSONWebTokenAPIView):
    """
    API View that checks the veracity of a token, returning the token if it
    is valid.
    """
    serializer_class = VerifyJSONWebTokenSerializer


class RefreshJSONWebToken(JSONWebTokenAPIView):
    """
    API View that returns a refreshed token (with new expiration) based on
    existing token

    If 'orig_iat' field (original issued-at-time) is found, will first check
    if it's within expiration window, then copy it to the new token
    """
    serializer_class = RefreshJSONWebTokenSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()






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

    safe_char_field = [
        'is_male', 'age', 'live_start_year'
        , 'personal_statement', 'vocation_type','native_province',
        'native_city', 'vocation_name', 'verify_telephone'
    ]

    safe_url_field = [
        'avatar_url', 'id_card_url'
    ]

    safe_list_field = [
        'languages', 'hobbies', 'characters'
    ]

    foreign_key = ['verify_city', 'verify_country']

    def get(self, request, format=None):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({"message":"can not access your profile, login first"}, status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        user = request.user
        errors = {}

        # foreign key
        try:
            location_city = request.DATA['location_city']

            city_list = City.objects.filter(name=location_city, country = user.location_country)

            if len(city_list) == 0:
                errors['location_city'] = ['city not found in country: %s'%user.location_country.name, ]
            else:
                user.location_city = city_list[0]

        except:
            print "Unexpected error:", sys.exc_info()

        # list field
        for f in self.safe_list_field:
            try:
                f_val = request.DATA[f]
                f_json_str = '[' + ", ".join(f_val)  + ']'
                setattr(user, f, f_json_str)
            except:
                pass


        # char field
        for f in self.safe_char_field:
            try:
                f_val = request.DATA[f]
                setattr(user, f, f_val)
            except:
                pass

        for f in self.safe_url_field:
            try:
                url_val = request.DATA[f]
                file_path = functions.get_file_path_from_url(url_val)
                image = Image.objects.get(address=file_path)
                if image is not None:
                    if image.upload_user == user or image.upload_user is None:
                        if f == 'avatar_url':
                            user.avatar = image
                        if f == 'id_card_url':
                            user.id_card = image

            except:
                pass
        try:
            user.save()
            u = UserSerializer(request.user)
            data = u.data
            data['errors'] = errors
            return Response(u.data, status.HTTP_200_OK)
        except:
            pass

        return Response(
                    {"message": "internal error, fail to update profile",
                         "errors": errors
                         }, status.HTTP_400_BAD_REQUEST)



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
                    User.objects.create_user(username=r.register_telephone, password=r.password
                                             , country=r.register_country, nickname=r.nickname,
                                             telephone = r.register_telephone)
                    data['username'] = r.register_telephone
                    return Response(data, status.HTTP_200_OK)
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