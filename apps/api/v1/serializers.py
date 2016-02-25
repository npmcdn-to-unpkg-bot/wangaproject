from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from apps.conta.models import UserProfile, Adresse
from apps.cursos.models import Curso, Turma, Modalidade
from django.contrib.auth.models import User
from rest_framework import permissions
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.utils.translation import ugettext as _

class UserSerializer(serializers.ModelSerializer):
    #code
    class Meta:
        model = User
        fields = ("id","first_name","last_name")

class UserAuth(serializers.ModelSerializer):
    #code
    class Meta:
        model = User
        fields = ("username","password")
    def Login(self,user):
        login(user)
        return user
        
        

class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields =("endereco_atual","numero","cep","cidade","estado")

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = UserProfile
        fields = ("id","user","nascimento","sexo")


class ModalidadeSerializer(serializers.ModelSerializer):
    professores = UserSerializer(many=True)
    class Meta:
        model = Modalidade
        fields = ("id","name","description","url", 'professores')


class CursoSerializer(serializers.ModelSerializer):
    modalidade = ModalidadeSerializer()
    class Meta:
        model = Curso
        fields = ("id","name","description",'modalidade','inicio_data','fim_data')


class TurmaSerialiser(serializers.ModelSerializer):
    #code
    detail = serializers.SerializerMethodField('detail_url')
    
    curso = CursoSerializer()
   
    def detail_url(self,Turma):
        return "http://localhost:8000/api/turma/"+str(Turma.id)+"/"
    
    class Meta():
        #code
        model = Turma
        fields = ("id","name","curso","inicio_data","inicio_hora", "fim_hora", "fim_data", "is_active","detail")


class CursoDetailSerializer(serializers.ModelSerializer):
    modalidade = ModalidadeSerializer()
    turmas = TurmaSerialiser(many=True)
    class Meta:
        model = Curso
        fields = ("id","name","description","modalidade","inicio_data","fim_data","turmas")

class TurmaDetailSerialiser(serializers.ModelSerializer):
    #code
    curso = CursoSerializer()
    members = UserSerializer(many=True)
    class Meta():
        #code
        model = Turma
        fields = ("id","name","curso","inicio_data","inicio_hora", "fim_hora", "fim_data", "is_active", "members")




