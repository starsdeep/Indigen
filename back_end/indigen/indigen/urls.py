from django.conf.urls import patterns, include, url
from indigen.views import IndexView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'indigen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include('location.urls')),
    url(r'^api/v1/', include('filesystem.urls')),
    url('^.*$', IndexView.as_view(), name='index')
)
