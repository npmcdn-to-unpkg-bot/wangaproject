from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
from django.template import Context
# Create your views here.
def Index(request):
    return render(request,"wanga/home.html")

def Login(request):
    return render(request,"wanga/login.html")

def Register(request):
    return render(request,"wanga/register.html")

def Cursos(request):
    return render(request,"wanga/cursos.html")

def Estilos(request):
    return render(request,"wanga/estilos.html")

def Zouk(request):
    return render(request,"wanga/zouk.html")

def Kizomba(request):
    return render(request,"wanga/kizomba.html")

def Eventos(request):
    return render(request,"wanga/eventos.html")


def Videos(request):
    return render(request,"wanga/videos.html")

def ContatoMail(request):
    nome = request.POST["nome"]
    email = request.POST["email"]
    assunto = request.POST["assunto"]
    message = request.POST["textmessage"]

    if nome and email and assunto and message:
        try:
            #send_mail("Your Subject", "This is a simple text email body.", "Yamil Asusta <hello@yamilasusta.com>", ["yamil@sendgrid.com"])

            # or
            #"nome: "+nome+ "<br>" + "email: "+ email +"<br>" +message,
            cont = {
                'nome': nome,
                'email': email,
                'message': message
            }
            html_content = get_template("wanga/email.html").render(Context(cont))
            mail = EmailMultiAlternatives(
                subject=assunto,

                body= html_content,
                from_email= 'support@wangaevents.com.br', #email,
                to=["wangaevents@gmail.com"],
                #headers={"Reply-To": "support@sendgrid.com"}
              )
            mail.content_subtype = 'html'
            mail.send()

        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return HttpResponseRedirect('/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')

def Contato(request):
    return render(request,"wanga/contato.html")

def Thanks(request):
    return render(request,"wanga/thanks.html")

def Agencia(request):
    return render(request,"wanga/agencia.html")

def Equipe(request):
    return render(request,"wanga/equipe.html")

def Sobre(request):
    return render(request,"wanga/about.html")

def CursoDetail(request):
    id= request.GET.get('id','')
    return render(request,"wanga/curso.html",{"id":id})

def Turma(request):
    id= request.GET.get('id','')

    return render(request,"wanga/turma.html",{"id":id})
