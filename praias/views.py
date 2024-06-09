from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Praia
from .models import Regiao
from .models import Servico

# Create your views here.

from django.http import HttpResponse

def index_view(request):
    context={
        'praias_lisboa':Praia.objects.filter(regiao__nome = 'Lisboa'),
        'praias_algarve': Praia.objects.filter(regiao__nome = 'Algarve'),
}
    return render(request, "praias/index.html", context)

def praia_view(request, praia_id):
    context = {
        'praia': Praia.objects.get(id= praia_id)
        }

    return render(request, "praias/praia.html", context)

