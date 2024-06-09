
from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('interesses/', views.interesses_view, name='interesses'),
    ]