__author__ = 'fucus'
from rest_framework import serializers
from filesystem.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image

