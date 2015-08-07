from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
from location.models import Country
from django.forms import forms

class MyUserManager(BaseUserManager):
    def create_user(self, username, password, country, nickname):

        country_obj = Country.objects.get(name=country)
        user = self.model(
            username = username,
            nickname = nickname,
            location_country = country_obj
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,password)
        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=30, null=False)
    email = models.EmailField(unique=True, null=True)
    telephone = models.CharField(unique=True, max_length=20, null=True)

    location_country = models.ForeignKey('location.Country', null=True, on_delete=models.SET_NULL)
    location_city = models.ForeignKey('location.City',null=True, on_delete=models.SET_NULL)
    nickname = models.CharField(max_length=20,null=True)

    avatar = models.ForeignKey('filesystem.Image', db_index=False, null=True, on_delete=models.SET_NULL)


    live_start_year = models.IntegerField(default=0, null=False)
    is_male = models.NullBooleanField()
    birthday = models.DateField(null=True)
    introduction = models.CharField(max_length=500,null=True)

    reply_average_second = models.IntegerField(null=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    age = models.CharField(max_length=8, null=True)

    USERNAME_FIELD = 'username'

    objects = MyUserManager()


    def clean(self):
        errors = {}
        telephone = self.telephone
        user = User.objects.filter(username=telephone)
        if len(user) > 0:
            errors["telephone"] = "telephone already exists, you can login directly"

        if self.country != "":
            country_list = Country.objects.filter(name=self.country)
            if len(country_list) == 0:
                errors["country"] = "county not found"
        raise forms.ValidationError(errors)

class Local(models.Model):
    user = models.OneToOneField('User')
    service_reply_average_second = models.IntegerField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10,null=True)
    service_introduction = models.CharField(max_length=300)
    id_card = models.ForeignKey('filesystem.Image', db_index=False, null=True, on_delete=models.SET_NULL)

