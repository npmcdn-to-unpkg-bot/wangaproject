from django.conf.urls import include, url,patterns
from .views import Login,Register,Logout,Profile, Login_page


urlpatterns = patterns('',
	(r'^login_page/$',Login_page),
	(r'^login/$',Login),
	(r'^register/$',Register),
	(r'^logout/$',Logout),
	(r'^profile/$',Profile),
	)
