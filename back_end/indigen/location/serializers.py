__author__ = 'fucus'
from rest_framework import serializers
from authentication.models import User, Local
from location.models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('full_name', 'name', 'telephone_prefix','capital_city')

