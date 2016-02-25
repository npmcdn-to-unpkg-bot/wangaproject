# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('endereco_atual', models.CharField(max_length=50, blank=True)),
                ('complemento', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=200, blank=True)),
                ('cidade', models.CharField(max_length=120, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(default=b'avatar.jpg', upload_to=b'profiles_image')),
                ('nascimento', models.DateField(blank=True)),
                ('sexo', models.CharField(max_length=1)),
                ('is_prof', models.BooleanField(default=False)),
                ('endereco', models.ForeignKey(to='conta.Adresse', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
