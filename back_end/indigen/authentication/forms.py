__author__ = 'fucus'
from django.forms import Form
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from authentication.models import User
from django.db import models
from django import forms

class RegisterModel(models.Model):
    class Meta:
        abstract = True
    telephone = models.CharField(max_length=30, null=False,blank=False)
    password = models.CharField(null=False,max_length=128, blank=False)

    def clean(self):
        telephone = self.telephone
        user = User.objects.filter(username=telephone)
        if len(user) > 0:
            raise forms.ValidationError({"telephone": "telephone already exists, you can login directly"})



