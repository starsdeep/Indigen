__author__ = 'fucus'
from rest_framework import serializers
from authentication.models import User, Local


class UserSerializer(serializers.ModelSerializer):
    password = serializers.models.TextField(null=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'last_login', 'telephone', 'location_country',
                  'location_city', 'nickname', 'avatar', 'live_start_year', 'is_male',
                  'birthday', 'introduction', 'reply_average_second')


class LocalSerializer(serializers.Serializer):
    price = serializers.DecimalField(decimal_places=2, max_digits=10, required=True)
    service_introduction = serializers.CharField(max_length=300, required=True)


    def create(self, validated_data):
        return Local.objects.create(**validated_data)

