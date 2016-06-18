from django.conf.urls import include, url,patterns
from django.conf import settings
from django.contrib.staticfiles import views
from django.views.static import serve
from .views import *
#from apps.account.views import Login

urlpatterns = [
    #(r'^$',Home),
    url(r'^$',Index),
    url(r'^cursos$',Cursos),
    url(r'^login$',Login),
    url(r'^register$',Register),
    url(r'^estilos$',Estilos),
    url(r'^estilos/zouk$',Zouk),
    url(r'^estilos/kizomba$',Kizomba),
    url(r'^turma/$',Turma),
    #url(r'^eventos$',Eventos),
    url(r'^videos$',Videos),
    url(r'^sobre$',Sobre),
    url(r'^curso/$',CursoDetail),

    url(r'^agencia$',Agencia),
    url(r'^equipe$',Equipe),
    url(r'^contato/$',Contato),
    url(r'^contato_mail/$',ContatoMail),
    url(r'^thanks/$',Thanks),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
]
