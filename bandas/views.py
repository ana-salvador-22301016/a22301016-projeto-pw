from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import BandaForm
from .forms import MusicaForm
from .forms import AlbumForm
from .models import Banda
from .models import Musica
from .models import Album

# Create your views here.

from django.http import HttpResponse

def index_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome')
    }
    return render(request, "bandas/bandas.html", context)


def bandas_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome')
    }
    return render(request, "bandas/bandas.html", context)

def banda_album_view(request, banda_id):
    context = {
        'banda': Banda.objects.get(id=banda_id),
        'albuns': Album.objects.filter(banda_id=banda_id),
    }
    return render(request, "bandas/banda_album.html", context)

def musicas_view(request):
    context = {
        'musicas': Musica.objects.all(),
    }
    return render(request, "bandas/musicas.html", context)

def albuns_view(request):
    context = {
        'album': Album.objects.all(),
    }
    return render(request, "bandas/albuns.html", context)

@login_required
@user_passes_test(lambda user: user.groups.filter(name='editores_bandas').exists())
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:albuns')
    context = {'form': form}
    return render(request, 'bandas/nova_banda.html', context)

@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda', banda_id=banda.id)
    else:
        form = BandaForm(instance=banda)
    context = {'form': form, 'banda': banda}
    return render(request, 'bandas/edita_banda.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:bandas')

@login_required
@user_passes_test(lambda user: user.groups.filter(name='editores_bandas').exists())
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES)
    if form.is_valid():
        album = form.save(commit=False)
        album.banda = banda
        album.save()
        return redirect('bandas:albuns')
    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)

@login_required
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:albuns', banda_id=album.banda.id)
    else:
        form = AlbumForm(instance=album)
    context = {'form': form, 'album': album}
    return render(request, 'bandas/edita_album.html', context)

@login_required
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas:albuns')

@login_required
@user_passes_test(lambda user: user.groups.filter(name='editores_bandas').exists())
def nova_musica_view(request, album_id):
    album = Album.objects.get(id=album_id)
    form = MusicaForm(request.POST or None, request.FILES)
    if form.is_valid():
        musica = form.save(commit=False)
        musica.album = album
        musica.save()
        return redirect('bandas:musicas')
    context = {'form': form}
    return render(request, 'bandas/nova_musica.html', context)

@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musicas')
    else:
        form = MusicaForm(instance=musica)
    context = {'form': form, 'musica': musica}
    return render(request, 'bandas/edita_musica.html', context)

@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandas:musicas')



def album_musicas_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    musicas = Musica.objects.filter(album=album)
    context = {
        'album': album,
        'musicas': musicas,
    }
    return render(request, 'bandas/musicas.html', context)
