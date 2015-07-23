# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('location', '0001_initial'),
        ('filesystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(to='filesystem.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='location_city',
            field=models.ForeignKey(to='location.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='location_country',
            field=models.ForeignKey(to='location.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='local',
            name='user',
            field=models.OneToOneField(to='authentication.User'),
            preserve_default=True,
        ),
    ]
