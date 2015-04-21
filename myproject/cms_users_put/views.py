from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
import feedparser

# Create your views here.

def mostrar(request, recurso):
    #SOLO PUEDES HACER POST SI ESTAS AUTENTICADO
    if request.user.is_authenticated():
        #salida = "Eres " + request.user.username + " " + "<a href='/logout'>logout</a>.  Puedes cambiar la page mediante un PUT<br><br>"
        if request.method == "PUT":
            p = Pages(name=recurso, page=request.body)
            p.save()
            return HttpResponse("guardada pagina, haz un get para comprobar")        
    else:
        pepe = "nada"
        #salida = "No estas logueado <a href='/admin/login/'>Login</a>. No puedes cambiar la page<br><br>"
    

    try:
        fila = Pages.objects.get(name=recurso)
        salida = fila.page
        if recurso == "css/main.css":
            return HttpResponse(salida, content_type="text/css")#type=text/css)
        else:
            return HttpResponse(salida)    
        
    except Pages.DoesNotExist:
        salida = "Page not found: " + recurso
        return HttpResponseNotFound(salida)


def todo(request):
    if request.user.is_authenticated():
        salida = "Eres " + request.user.username + " " + "<a href='/logout'>logout</a><br><br>"
    else:
        salida = "No estas logueado <a href='/admin/login/'>Login</a><br><br>"
            
    lista = Pages.objects.all()
    salida += "Esto es lo que tenemos:<ul>"
    for fila in lista:
        salida += "<li>" + fila.name + "->" + str(fila.page) + " "
    salida += "</ul>"
    return HttpResponse(salida)


def twitter(request, recurso):
    url = "https://twitrss.me/twitter_user_to_rss/?user=" + recurso
    parseo = feedparser.parse(url)
    salida = "<h1>Ultimos 5 Twits de: @" + recurso + "</h1><br><ul>"
    for i in range(0,5):
        salida += "<li>" + str(parseo.entries[i].title)
    return HttpResponse(salida)
