from django.urls import path

from . import views

app_name= 'praias'

urlpatterns = [
    path('', views.index_view, name= "praiaindex"),
    path('praia/<int:praia_id>', views.praia_view, name="praia"),

]