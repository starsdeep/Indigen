# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_reply_average_second', models.IntegerField(null=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('service_introduction', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=30)),
                ('email', models.EmailField(max_length=75, unique=True, null=True)),
                ('telephone', models.CharField(max_length=20, unique=True, null=True)),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('live_start_year', models.IntegerField()),
                ('is_male', models.BooleanField()),
                ('birthday', models.DateField()),
                ('introduction', models.CharField(max_length=500)),
                ('reply_average_second', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
