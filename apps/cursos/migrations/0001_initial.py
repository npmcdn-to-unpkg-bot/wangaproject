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
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('inicio_data', models.DateField(blank=True)),
                ('fim_data', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateField()),
                ('aluno', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True)),
                ('professores', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('inicio_data', models.DateField(blank=True)),
                ('inicio_hora', models.TimeField(blank=True)),
                ('fim_hora', models.TimeField(blank=True)),
                ('fim_data', models.DateField(blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(to='cursos.Curso')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='cursos.Membership')),
            ],
            options={
                'ordering': ['created', 'is_active'],
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='turma',
            field=models.ForeignKey(to='cursos.Turma'),
        ),
        migrations.AddField(
            model_name='curso',
            name='modalidade',
            field=models.ForeignKey(to='cursos.Modalidade'),
        ),
    ]
