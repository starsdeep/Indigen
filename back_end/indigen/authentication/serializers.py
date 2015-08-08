__author__ = 'fucus'
from rest_framework import serializers
from authentication.models import User, Local
from filesystem.models import Image

class UserSerializer(serializers.ModelSerializer):
    password = serializers.models.TextField(null=False)

    @property
    def data(self):
        self._data = super(UserSerializer, self).data
        data = self._data
        user = User.objects.get(username=data['username'])
        try:
            avatar =  Image.objects.get(id=data['avatar'])
            data['avatar_url'] = avatar.address.url
        except:
            pass

        try:
            data['id_card_url'] = user.id_card.address.url
        except:
            pass

        try:
            data['service_introduction'] = user.local.service_introduction
        except:
            pass

        try:
            data['location_country'] = user.location_country.name
        except:
            pass

        try:
            data['location_city'] = user.location_city.name
        except:
            pass

        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'last_login', 'register_telephone', 'register_country'
                  , 'nickname', 'avatar', 'live_start_year', 'is_male',
                  'birthday', 'personal_statement', 'reply_average_second','age','vocation_type'
                  ,'native_province','native_city','vocation_name','verify_city', 'verify_country',
                  'languages', 'hobbies', 'characters', 'verify_telephone')



class LocalSerializer(serializers.Serializer):
    price = serializers.DecimalField(decimal_places=2, max_digits=10, required=True)
    service_introduction = serializers.CharField(max_length=300, required=True)


    def create(self, validated_data):
        return Local.objects.create(**validated_data)

