# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.gallerie.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pasta', models.CharField(unique=True, max_length=10)),
                ('titulo', models.CharField(max_length=20)),
                ('descricao', models.TextField(max_length=100)),
                ('publicar', models.BooleanField(default=False)),
                ('autor', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-publicar', '-created'],
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albuns',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=10, blank=True)),
                ('image', models.FileField(upload_to=apps.gallerie.models.saving_to_album)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('isCover', models.BooleanField(default=False)),
                ('album', models.ForeignKey(to='gallerie.Album')),
            ],
            options={
                'ordering': ['-isCover'],
            },
        ),
    ]
