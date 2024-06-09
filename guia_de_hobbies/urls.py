
from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'guia_de_hobbies'

urlpatterns = [
    path('hobbies/', views.hobbies_view, name='hobbies'),
    path('hobbies_criancas/', views.hobbies_criancas_view, name='hobbies_criancas'),
    path('hobbies_adolescentes/', views.hobbies_adolescentes_view, name='hobbies_adolescentes'),
    path('hobbies_jovens/', views.hobbies_jovens_view, name='hobbies_jovens'),
    path('hobbies_idosos/', views.hobbies_idosos_view, name='hobbies_idosos'),
    ]