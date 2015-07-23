from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)


class Country(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=30, null=False)
    capital_city = models.CharField(max_length=30, null=True)
    telephone_prefix = models.CharField(max_length=10)



class Language(models.Model):
    name = models.CharField(max_length=50)

class UserLanguage(models.Model):
    user = models.ForeignKey('authentication.User')
    language = models.ForeignKey('Language')