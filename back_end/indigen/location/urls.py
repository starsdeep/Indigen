__author__ = 'fucus'

from django.conf.urls import url
from location.views import CountryViewSet



country_list = CountryViewSet.as_view()


urlpatterns = [
    url('^countrys/$', country_list),
]
