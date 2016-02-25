# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modalidade',
            name='professores',
        ),
        migrations.AddField(
            model_name='modalidade',
            name='professores',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
