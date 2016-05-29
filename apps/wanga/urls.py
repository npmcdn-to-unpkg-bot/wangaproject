from django.conf.urls import include, url,patterns
from django.conf import settings
from django.contrib.staticfiles import views
from .views import *
#from apps.account.views import Login

urlpatterns = patterns('',
    #(r'^$',Home),
    (r'^$',Index),
    (r'^cursos$',Cursos),
    (r'^login$',Login),
    (r'^register$',Register),
    (r'^estilos$',Estilos),
    (r'^turma/$',Turma),
    #(r'^eventos$',Eventos),
    (r'^videos$',Videos),
    (r'^about$',About),
    (r'^curso/$',CursoDetail),
    
    (r'^agencia$',Agencia),
    (r'^equipe$',Equipe),
    (r'^contato/$',Contato),
    (r'^contato_mail/$',ContatoMail),
    (r'^thanks/$',Thanks),
)
if settings.DEBUG:
    urlpatterns += patterns('',
       # url((r'^media/(?P<path>.*)$', views.serve),
       # {'document_root': settings.MEDIA_ROOT})
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
)
