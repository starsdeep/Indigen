from django.conf.urls import patterns, include, url
from indigen.views import IndexView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'indigen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include('location.urls')),
    url(r'^api/v1/', include('filesystem.urls')),
] + static(settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )

urlpatterns.append(url('^.*$', IndexView.as_view(), name='index'))

