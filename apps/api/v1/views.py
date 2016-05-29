from django.shortcuts import render, redirect,HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, Http404
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from apps.cursos.models import Modalidade,Curso,Turma
from apps.conta.models import UserProfile
from .serializers import *
from rest_framework.pagination import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from django.conf import settings


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    #max_page_size = 20

# Create your views here.
class Modalidade_list(APIView):
    """ Listar as modalidade disponiveis """
    def get(self, request,format=None):
        modals = Modalidade.objects.all()
        serializer = ModalidadeSerializer(modals, many=True)
        return Response(serializer.data)


class CursosView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_object(self, pk):
        try:
            curso = Curso.objects.get(pk=int(pk))
            return curso
        except Curso.DoesNotExist:
            raise Http404

    """def list(self, request,format=None):

        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data) """

    def retrieve(self, request,pk, format=None):
        """ Detalhe de um unico curso """
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

class TurmasView(viewsets.ViewSet):
    queryset = Turma.objects.all()
    """ Lista dos cursos disponiveis """
    def list(self, request, format=None):
        #name = request.GET.get('name','')
        turmas = Turma.objects.all()#.filter(modalidade__name=name)
        serializer = TurmaSerialiser(turmas, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            turma = Turma.objects.get(pk=int(pk))
            return turma
        except Turma.DoesNotExist:
            raise Http404
    def retrieve(self, request, pk=None,format=None):
        """ Detalhes de uma turma """
        curso = get_object_or_404(Curso, pk=pk)
        turmas = Turma.objects.all().filter(curso=curso)
        serializer = TurmaSerialiser(turmas,many=True)
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
