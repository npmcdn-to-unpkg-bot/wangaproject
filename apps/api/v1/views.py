from django.shortcuts import render, redirect,HttpResponse
from django.http import Http404
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.cursos.models import Modalidade,Curso,Turma
from apps.conta.models import UserProfile
from .serializers import (ModalidadeSerializer,CursoSerializer, TurmaSerialiser, TurmaDetailSerialiser,
    CursoDetailSerializer,ProfileSerializer, UserAuth, UserSerializer)
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from django.conf import settings


# Create your views here.
class Modalidade_list(APIView):
    """ Listar as modalidade disponiveis """
    def get(self, request,format=None):
        modals = Modalidade.objects.all()
        serializer = ModalidadeSerializer(modals, many=True)
        return Response(serializer.data)


class CursosList(APIView):
    """ Lista dos cursos disponiveis """
    def get(self, request,format=None):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

class CursoDetail(APIView):
    """ Detalhe de um unico curso """
    def get_object(self, pk):
        try:
            curso = Curso.objects.get(pk=int(pk))
            return curso
        except Curso.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        #name= request.GET.get('name','')
        curso = self.get_object(pk)
        serializer = CursoDetailSerializer(curso)
        return Response(serializer.data)
    
class UserList(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    """ lista dos usuarios usuario """
    def get(self, request , format=None):    
        users = User.objects.all()
        serializer =UserSerializer(users, many=True)
        return Response(serializer.data)

class  ProfilDetail(APIView):
    """ perfil de um usuario """
    def get_object(self, pk):
        try:
            user= User.objects.get(pk=int(pk))
            if(user.is_active):
                return user
            else:
                raise Http404
        except Turma.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)    
        profil = UserProfile.objects.get(user=user)
        if profil:
            serializer =ProfileSerializer(profil)
            return Response(serializer.data)
        else:
            return Response(serializer.data)

class TurmasList(APIView):
    """ Lista dos cursos disponiveis """
    def get(self, request, format=None):
        #name = request.GET.get('name','')
        turmas = Turma.objects.all()#.filter(modalidade__name=name)
        serializer = TurmaSerialiser(turmas, many=True)
        return Response(serializer.data)

class TurmaDetail(APIView):
    """ Detalhes de uma turma """
    def get_object(self, pk):
        try:
            turma = Turma.objects.get(pk=int(pk))
            return turma
        except Turma.DoesNotExist:
            raise Http404
    
    def get(self, request, pk,format=None):    
        turma = self.get_object(pk)
        serializer = TurmaDetailSerialiser(turma)
        return Response(serializer.data)


class UserHistory(APIView):
    """ turma nos quais o usuario e membro ou esta inscrito """
    def get(self,request,pk,format=None):
        user = User.objects.get(id= int(pk))
        turmas = user.turma_set.all()
        serializer = TurmaSerialiser(turmas,many=True)
        return Response(serializer.data)
class UserAvailable(APIView):
    """ Detalhes do usuario logado """

    def get(self,request):
        user = self.request.user
        if(user):
            serializer = UserSerializer(user)
            return Response(serializer.data);

