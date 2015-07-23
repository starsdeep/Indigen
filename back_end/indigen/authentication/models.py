from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=30, null=False)
    email = models.EmailField(unique=True, null=True)
    telephone = models.CharField(unique=True, max_length=20, null=True)

    location_country = models.ForeignKey('location.Country',null=False)
    location_city = models.ForeignKey('location.City',null=True)
    nickname = models.CharField(max_length=20,null=True)

    avatar = models.ForeignKey('filesystem.Image', db_index=False)
    live_start_year = models.IntegerField()
    is_male = models.BooleanField(null=False)
    birthday = models.DateField()
    introduction = models.CharField(max_length=500)

    reply_average_second = models.IntegerField()

class Local(models.Model):
    user = models.OneToOneField('User')
    service_reply_average_second = models.IntegerField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    service_introduction = models.CharField(max_length=300)
