from django.db import models
#from apps.conta.models import UserProfile
from django.contrib.auth.models import User
# Create your models here.

class Modalidade(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	url = models.URLField(blank=True)
	professores = models.ManyToManyField(User)

	def __str__(self):
		return self.name

class Curso(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	#url = models.URLField(blank=True)
	modalidade = models.ForeignKey(Modalidade)
	inicio_data = models.DateField(auto_now_add= False, blank=True)
	fim_data = models.DateField(auto_now_add= False, blank=True)

	def __str__(self):
		return self.name

class Turma(models.Model):
	#code
	name = models.CharField(max_length=120)
	curso = models.ForeignKey(Curso, related_name='turmas')
	members = models.ManyToManyField(User, through='Membership')
	inicio_data = models.DateField(auto_now_add= False, blank=True)
	inicio_hora = models.TimeField(auto_now_add=False, blank=True)
	fim_hora = models.TimeField(auto_now_add=False, blank=True)
	fim_data = models.DateField(auto_now_add= False, blank=True)
	is_active=models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']
	def __str__(self):
		return self.name



class Membership(models.Model):
	aluno = models.ForeignKey(User)
	turma = models.ForeignKey(Turma)
	date_joined = models.DateField()
