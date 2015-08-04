from django.shortcuts import render
from authentication.views import BaseModelView
from location.models import Country
from location.serializers import CountrySerializer
# Create your views here.

class CountryViewSet(BaseModelView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer