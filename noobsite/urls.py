# urls.py

from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('index/', views.index_view),
    path("<str:name>", views.bom_dia_amigos_view, name= "lucio" ),
    path("nada/", views.nada_view, name= "nada"),
    path("imagina/", views.imagina_view, name= "imagina"),

]