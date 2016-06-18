from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from localflavor.br.forms import BRPhoneNumberField, BRCPFField, BRZipCodeField, BRStateChoiceField
# Create your models here.
class Adresse(models.Model):
	endereco_atual = models.CharField(max_length=50,blank=True)
	numero = forms.RegexField(regex=r'^\+?1?\d{2,4}$' )
	complemento = models.CharField(max_length=20)
	bairro = models.CharField(max_length=200,blank=True)
	cep = BRZipCodeField()
	cidade = models.CharField(max_length=120,blank=True)
	estado = BRStateChoiceField( )


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#avatar = models.ImageField(upload_to='profiles_image', blank=True, null=True)
	nascimento = models.DateField(auto_now_add= False, blank=True)
	sexo = models.CharField(max_length=1)
	#cidade = models.CharField(max_length=120)
	telefone = BRPhoneNumberField( )
	cpf = BRCPFField( )
	endereco = models.ForeignKey(Adresse, blank=True)
	is_prof = models.BooleanField(default=False)
	def __str__(self):
		return self.user.username

"""
#estado = BRStateChoiceField( blank=True)
	COMO_soube_do_curso = (
		('Pela internet'),
		('Por amigos(as)'),
		('Por panfletos'),
	)
	#como_soube_do_curso = models.CharField(max_length=50,choices=COMO_soube_do_curso)
	conhecimento_de_danca =(
		('Zouk'),
		('Salsa'),
		('Kizomba'),
		('Forro'),
		('Sambo'),
		('Outro'),
		)
	#danca = models.CharField(max_length=50, choices=conhecimento_de_danca)
	expectativas = models.TextField()
"""
