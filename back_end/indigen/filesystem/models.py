from django.db import models

# Create your models here.


class File(models.Model):

    class Meta:
        abstract = True

    upload_user = models.ForeignKey('authentication.User',on_delete=models.SET_NULL,null=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=30, null=True)
    size = models.IntegerField(null=False)
    address = models.FileField(upload_to="documents/%Y/%m/%d")


class Image(File):
    class Meta:
        abstract = False



class Video(File):
    class Meta:
        abstract = False

    height = models.IntegerField(null=False)
    width = models.IntegerField(null=False)
    length = models.IntegerField(null=False)


class Audio(File):
    class Meta:
        abstract = False
    length = models.IntegerField(null=False)