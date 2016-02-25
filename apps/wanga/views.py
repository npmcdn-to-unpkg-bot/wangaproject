from django.shortcuts import render
#from .models import Index, Cursos, Eventos, Videos, Contact, About
# Create your views here.
def Index(request):
    return render(request,"wanga/index.html")

def Cursos(request):
    return render(request,"wanga/cursos.html")
def Modals(request):
    return render(request,"wanga/modals.html")

def Eventos(request):
    return render(request,"wanga/eventos.html")


def Videos(request):
    return render(request,"wanga/videos.html")


def Contact(request):
    return render(request,"wanga/contact.html")

def Agencia(request):
    return render(request,"wanga/agencia.html")

def Equipe(request):
    return render(request,"wanga/equipe.html")

def About(request):
    return render(request,"wanga/about.html")

def CursoDetail(request):
    id= request.GET.get('id','')
    return render(request,"wanga/curso.html",{"id":id})

def Turma(request):
    id= request.GET.get('id','')
    
    return render(request,"wanga/turma.html",{"id":id})