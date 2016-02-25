from django.db import models
#from string import join
from django.conf import settings
import os


# Create your models here.

class AlbumQuerySet(models.QuerySet):
    def publicado(self):
        return self.filter(publicar=True)


class Album(models.Model):
	pasta     = models.CharField(max_length = 10,blank=False, unique=True)
	titulo    = models.CharField(max_length = 20, blank=False)
	descricao = models.TextField(max_length=100, blank=False)
	publicar  = models.BooleanField(default=False)
	autor     = models.CharField(max_length=50, blank=False)
	created = models.DateTimeField(auto_now_add=True, blank=True)
	objects  = AlbumQuerySet.as_manager()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name        = "Album"
		verbose_name_plural = "Albuns"
		ordering			= ["-publicar","-created"]



	def create(self):
		if not os.path.exists(os.path.join(MEDIA_ROOT,self.pasta)):
			os.makedirs(os.path.join(settings.MEDIA_ROOT,self.pasta))



			
def saving_to_album(instance, filename):
    return '/'.join([instance.album.pasta, filename])


class Photo(models.Model):
	nome    = models.CharField(max_length=10, blank=True)
	album   = models.ForeignKey(Album,blank=False)
	image   = models.FileField(upload_to=saving_to_album)
	created = models.DateTimeField(auto_now_add=True)
	#width   = models.IntegerField(blank=True, null=True)
	#height  = models.IntegerField(blank=True, null=True)
	isCover = models.BooleanField(default=False)

	def __str__(self):
		return self.image.name

	class Meta:
		ordering = ["-isCover"]