from django.conf.urls import include, url,patterns
from .views import Cursos

urlpatterns = patterns('',
	(r'^api/cursos$',Cursos),

	)