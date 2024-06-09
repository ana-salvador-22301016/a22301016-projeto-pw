from django.urls import path
from . import views

app_name = 'meteo'
urlpatterns = [
    path('', views.meteo_view, name="meteo"),

]