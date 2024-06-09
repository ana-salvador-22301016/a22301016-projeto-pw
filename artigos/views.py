from django.shortcuts import render,get_object_or_404
from .models import Artigos


def index_view(request):
    context = {
        'artigos': Artigos.objects.all(),
    }
    return render(request, 'artigos/index.html', context)

def detail_view(request, artigo_id):
    artigo = get_object_or_404(Artigos, pk=artigo_id)
    return render(request, 'artigos/detail.html', {'artigo': artigo})




