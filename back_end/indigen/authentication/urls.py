__author__ = 'fucus'

from django.conf.urls import url
from authentication import views
from authentication.views import UserViewSet

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'

})


urlpatterns = [
    url('^login/$', views.login),
    url('^logout/$', views.logout),
    url('^users/password/$',views.password_update),
    url(r'^users/$', user_list),
    url(r'^users/(?P<pk>.+)/$', user_detail),
    url('^profile/$', views.profile)
]
