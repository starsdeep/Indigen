from django.conf.urls import patterns, include, url
from django.contrib import admin
from indigen.views import IndexView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'indigen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index')
)
