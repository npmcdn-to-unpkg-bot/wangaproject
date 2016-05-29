from django.conf.urls import include, url,patterns
from django.conf import settings
from django.contrib.staticfiles import views
from .views import Galeria,album


urlpatterns = patterns('apps.gallerie.views',
    
    (r'^gal/galeria$',Galeria),
    #(r'^videos$',Videos),
    (r'^gal/album/(?P<pasta>[\w\-]+)$',album),
)