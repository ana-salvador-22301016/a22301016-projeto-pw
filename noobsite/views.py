from django.shortcuts import render

# Create your views here.
# project/views.py

from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def bom_dia_amigos_view(request, name):
    return HttpResponse(f"bom dia, {name.capitalize()}!")

def nada_view(request):
    return HttpResponse("Não sei mais o que fazer, mas devo fazer, enfim...")

def imagina_view(request):
    return HttpResponse("Imagina: tu e eu sentados a programar sem o intellij e sim com pythonnywhere")
