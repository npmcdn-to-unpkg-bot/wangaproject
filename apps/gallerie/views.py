from django.shortcuts import render
from .models import Album, Photo
# Create your views here.

def Galeria(request):
	albuns=[]
	al = Album.objects.publicado()
	for a in al:
		albuns.append({"album":a,"cover":a.photo_set.filter(isCover=True)})
	return render(request,"gallerie/galeria.html",{"albuns":albuns})

def album(request,pasta):
	alb = Album.objects.filter(pasta=pasta)
	for a in alb:
		photos=a.photo_set.all()
	return render(request,"gallerie/album.html",{"photos":photos})
