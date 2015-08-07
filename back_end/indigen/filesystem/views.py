from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from authentication.serializers import UserSerializer
from authentication.models import User, Local
import sys

from filesystem.models import File
from filesystem.models import Image
from filesystem.serializers import ImageSerializer
# Create your views here.


@api_view(('POST',) )
@csrf_exempt
def upload_file(request):

    # test no login upload
    if not request.user.is_anonymous():
        try:
            image = Image(address=request.FILES.items()[0][1])
            image.size = image.address.size
            image.upload_user = request.user
            try:
                image.save()
            except:
                print "Unexpected error:", sys.exc_info()[0]
            serializer = ImageSerializer(image)
            return Response(serializer.data)
        except:
            return Response({"message": "fail to upload"}
                            , status.HTTP_400_BAD_REQUEST)

    return Response({"message": "please login before upload file"})





class AvatarUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def post(self, request):
        try:
            image = Image(address=request.FILES.items()[0][1])
            image.size = image.address.size
            image.upload_user = request.user
            try:
                image.save()
                user = request.user
                user.avatar = image
                user.save()
            except:
                return Response({"message": "fail to upload avatar"}
                            , status.HTTP_400_BAD_REQUEST)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response({"message": "fail to upload avatar"}
                            , status.HTTP_400_BAD_REQUEST)



class IdCardUploadView(APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            image = Image(address=request.FILES.items()[0][1])
            image.size = image.address.size
            image.upload_user = request.user
            try:
                image.save()
                user = request.user
                try:
                    local = user.local
                except:
                    local = Local(user=user)
                local.id_card = image
                local.save()
            except:
                return Response({"message": "fail to upload id card"}
                            , status.HTTP_400_BAD_REQUEST)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response({"message": "fail to upload id card"}
                            , status.HTTP_400_BAD_REQUEST)



class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)


    def post(self, request):
        try:
            image = Image(address=request.FILES.items()[0][1])
            image.size = image.address.size
            image.upload_user = request.user
            try:
                image.save()
            except:
                print "Unexpected error:", sys.exc_info()[0]
            serializer = ImageSerializer(image)
            return Response(serializer.data)
        except:
            return Response({"message": "fail to upload"}
                            , status.HTTP_400_BAD_REQUEST)