from django.shortcuts import render
from authentication.views import BaseModelView
from location.models import Country
from location.serializers import CountrySerializer

from rest_framework import generics
from rest_framework import filters

# Create your views here.

class CountryViewSet(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name', 'telephone_prefix')