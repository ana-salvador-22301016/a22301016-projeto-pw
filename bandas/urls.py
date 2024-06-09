from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view),
    path('bandas/<int:banda_id>/banda', views.banda_album_view, name="banda_album"),
    path('bandas/', views.bandas_view, name="bandas"),
    path('banda_album/<int:banda_id>/', views.banda_album_view, name="banda_album"),
    path('albuns/', views.index_view, name="albuns"),
    path('album/', views.albuns_view, name="album"),
    path('musicas/', views.musicas_view, name="musicas"),
    path('nova_banda/', views.nova_banda_view, name="nova_banda"),
    path('bandas/<int:banda_id>/edita_banda', views.edita_banda_view, name="edita_banda"),
    path('bandas/<int>banda_id>/apaga_banda', views.apaga_banda_view, name="apaga_banda"),
    path('novo_album/<int:banda_id>', views.novo_album_view, name="novo_album"),
    path('edita_album/<int:album_id>', views.edita_album_view, name="edita_album"),
    path('apaga_album/<int:album_id>', views.apaga_album_view, name="apaga_album"),
    path('nova_musica/<int:album_id>', views.nova_musica_view, name="nova_musica"),
    path('edita_musica/<int:musica_id>', views.edita_musica_view, name="edita_musica"),
    path('apaga_musica/<int:musica_id>', views.apaga_musica_view, name="apaga_musica"),
     path('musicas/<int:album_id>/', views.album_musicas_view, name="album_musicas"),  # Nova URL
]
