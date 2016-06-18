from django.conf.urls import include, url,patterns
from  rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'turmas', TurmasView)
router.register(r'cursos', CursosView)
urlpatterns = [

    url(r'^user/$',UserAvailable.as_view()),
    url(r'^modals/$',Modalidade_list.as_view()),
    #(r'^cursos/$',CursosList.as_view()),
    #(r'^curso/(?P<pk>[0-9]+)/$',CursoDetail.as_view()),
    #(r'^turmas/$',TurmasList.as_view()),
    url(r'^profil/(?P<pk>[0-9]+)/$',ProfilDetail.as_view()),
    #(r'^turma/(?P<pk>[0-9]+)/$', TurmaDetail.as_view()),
    url(r'^user_history/(?P<pk>[0-9]+)/$', UserHistory.as_view()),

]

urlpatterns += [
	#url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += router.urls
