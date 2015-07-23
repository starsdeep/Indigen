# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_datetime', models.DateTimeField(auto_now_add=True)),
                ('format', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('file_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='filesystem.File')),
                ('length', models.IntegerField()),
            ],
            options={
            },
            bases=('filesystem.file',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('file_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='filesystem.File')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
            options={
            },
            bases=('filesystem.file',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('image_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='filesystem.Image')),
                ('length', models.IntegerField()),
            ],
            options={
            },
            bases=('filesystem.image',),
        ),
        migrations.AddField(
            model_name='file',
            name='upload_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='authentication.User', null=True),
            preserve_default=True,
        ),
    ]
