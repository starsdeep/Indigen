__author__ = 'fucus'

from django.conf.urls import url
from authentication import views
from authentication.views import UserViewSet

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    url('^login$', views.login),
    url('^logout$', views.logout),
    url(r'^users/$', user_list),
    url(r'^users/(?P<pk>.+)/$', user_detail)
]