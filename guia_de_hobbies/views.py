from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hobbies_view(request):
    return render(request, "hobbies/hobbies.html")

def hobbies_criancas_view(request):
    return render(request, "hobbies/hobbies_criancas.html")

def hobbies_adolescentes_view(request):
    return render(request, "hobbies/hobbies_adolescentes.html")

def hobbies_jovens_view(request):
    return render(request, "hobbies/hobbies_jovens.html")


def hobbies_idosos_view(request):
    return render(request, "hobbies/hobbies_idosos.html")
