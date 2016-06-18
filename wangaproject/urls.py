"""wangaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import  static

urlpatterns = [
    url(r'^',include('apps.wanga.urls')),
    url(r'^v1/',include('apps.api.v1.urls',namespace='v1')),
    #url(r'^',include('apps.gallerie.urls')),
    #url(r'^',include('apps.cursos.api')),
    #url(r'^conta/',include('apps.conta.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
