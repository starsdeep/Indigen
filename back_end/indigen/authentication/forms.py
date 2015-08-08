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

    register_telephone = models.CharField(max_length=20, null=True)
    nickname = models.CharField(max_length=20,null=False,blank=False,default="")
    password = models.CharField(max_length=128,blank=False,default="")
    register_country = models.CharField(max_length=30, default="", blank=False)

    def to_python(self, value):
        try:
            return value[0]
        except:
            return value

    def full_clean(self, exclude=None, validate_unique=True):

        for f in self._meta.fields:

            raw_value = getattr(self, f.attname)
            try:
                setattr(self, f.attname, raw_value[0])
            except:
                pass

        models.Model.full_clean(self, exclude=None, validate_unique=True)

    def clean(self):
        errors = {}
        telephone = getattr(self, 'register_telephone')
        user = User.objects.filter(username=telephone)
        if len(user) > 0:
            errors["register_telephone"] = "telephone already exists, you can login directly"

        if self.register_country != "":
            country_list = Country.objects.filter(name=self.register_country)

            if len(country_list) == 0:
                errors["register_country"] = "country not found"
        raise forms.ValidationError(errors)