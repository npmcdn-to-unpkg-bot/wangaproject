from django.conf.urls import include, url,patterns
from .views import (Modalidade_list,CursosList, TurmasList, TurmaDetail, UserHistory, ProfilDetail, 
	CursoDetail, UserAvailable)


urlpatterns = patterns('',
    
    (r'^user/$',UserAvailable.as_view()),
    (r'^modals/$',Modalidade_list.as_view()),
    (r'^cursos/$',CursosList.as_view()),
    (r'^curso/(?P<pk>[0-9]+)/$',CursoDetail.as_view()),
    (r'^turmas/$',TurmasList.as_view()),
    (r'^profil/(?P<pk>[0-9]+)/$',ProfilDetail.as_view()),
    (r'^turma/(?P<pk>[0-9]+)/$', TurmaDetail.as_view()),
    (r'^user_history/(?P<pk>[0-9]+)/$', UserHistory.as_view()),
    
)

urlpatterns += [
	#url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]