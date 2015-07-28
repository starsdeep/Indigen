__author__ = 'fucus'
from rest_framework import serializers
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.models.TextField(null=False)
    class Meta:
        model = User
        fields = ('username', 'nickname', 'birthday')