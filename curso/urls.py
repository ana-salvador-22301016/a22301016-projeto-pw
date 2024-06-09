from django.urls import path

from . import views

app_name= 'curso'

urlpatterns = [
    path('curso/', views.curso_view, name="curso"),
    path('disciplina_curso/<int:curso_id>', views.disciplina_curso_view, name="disciplina_curso"),
    path('projeto/', views.projeto_view, name="projeto"),
    path('', views.inicio, name='inicio'),
    path('novo_curso/', views.novo_curso_view, name="novo_curso"),
    path('curso/<int:curso_id>/edita_curso', views.edita_curso_view,name="edita_curso"),
    path('curso/<int:curso_id>/apaga_curso', views.apaga_curso_view,name="apaga_curso"),
    path('detalhe_disciplina/<int:disciplina_id>',views.detalhes_disciplina_view, name= "detalhe_disciplina"),

    path('disciplina/<int:disciplina_id>/', views.disciplina_view, name="disciplina"),
    path('nova_disciplina/<int:curso_id>', views.nova_disciplina_view, name="nova_disciplina"),
    path('edita_disciplina/<int:disciplina_id>/', views.edita_disciplina_view, name='edita_disciplina'),
    path('apaga_disciplina/<int:disciplina_id>', views.apaga_disciplina_view,name="apaga_disciplina"),

    path('novo_projeto/<int:disciplina_id>', views.novo_projeto_view, name="novo_projeto"),
    path('edita_projeto/<int:projeto_id>', views.edita_projeto_view,name="edita_projeto"),
    path('apaga_projeto/<int:projeto_id>', views.apaga_projeto_view,name="apaga_projeto"),


]