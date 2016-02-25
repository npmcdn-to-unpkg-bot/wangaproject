from django.conf.urls import include, url,patterns
from django.conf import settings
from django.contrib.staticfiles import views
from .views import Index,Videos,About,Contact, CursoDetail, Turma ,Cursos, Modals, Agencia, Equipe
#from apps.account.views import Login

urlpatterns = patterns('',
    #(r'^$',Home),
    (r'^$',Index),
    (r'^cursos$',Cursos),
    (r'^modals$',Modals),
    (r'^turma/$',Turma),
    #(r'^eventos$',Eventos),
    (r'^videos$',Videos),
    (r'^about$',About),
    (r'^curso/$',CursoDetail),
    (r'^contact$',Contact),   
    (r'^agencia$',Agencia),
    (r'^equipe$',Equipe),
)
if settings.DEBUG:
    urlpatterns += patterns('',
       # url((r'^media/(?P<path>.*)$', views.serve),
       # {'document_root': settings.MEDIA_ROOT})
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
)
