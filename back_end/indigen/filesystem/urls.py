__author__ = 'fucus'

from django.conf.urls import url
from filesystem import views
from filesystem.views import FileUploadView
from filesystem.views import AvatarUploadView
from filesystem.views import IdCardUploadView


urlpatterns = [
    url('^upload_avatar[/]*$', AvatarUploadView.as_view()),
    url('^upload_id_card[/]*$', IdCardUploadView.as_view()),
    url('^upload_file[/]*$', FileUploadView.as_view()),
]
