__author__ = 'fucus'

from django.conf.urls import url
from filesystem import views
from filesystem.views import FileUploadView



urlpatterns = [
    url('^upload_file/$', FileUploadView.as_view()),
]
