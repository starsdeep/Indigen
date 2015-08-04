__author__ = 'fucus'
from django.forms import Form
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from authentication.models import User
from django.db import models
from django import forms
from base_class.base import BaseInitWithDic
from location.models import Country

class RegisterModel(models.Model):
    class Meta:
        abstract = True

    telephone = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=20,null=False,blank=False,default="")
    password = models.CharField(max_length=128,blank=False,default="")
    country = models.CharField(max_length=30, default="", blank=False)



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