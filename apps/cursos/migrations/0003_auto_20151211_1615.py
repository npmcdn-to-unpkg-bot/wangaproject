# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20151211_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='curso',
            field=models.ForeignKey(related_name='turmas', to='cursos.Curso'),
        ),
    ]
