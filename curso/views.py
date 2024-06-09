from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import CursoForm
from .forms import DisciplinaForm
from .forms import ProjetoForm
from .models import Curso
from .models import Disciplina
from .models import Projeto


# Create your views here.

from django.http import HttpResponse

def curso_view(request):
    context = {
        'cursos': Curso.objects.all().order_by('nome'),
    }
    return render(request, "curso/curso.html", context)


def inicio(request):
    context = {
        'cursos': Curso.objects.all().order_by('nome'),
    }
    return render(request, "curso/curso.html", context)


def disciplina_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    disciplinas = curso.disciplina_set.all().order_by('nome')  # Obtém disciplinas associadas ao curso
    context = {
        'curso': curso,
        'disciplinas': disciplinas,
    }
    return render(request, "curso/disciplina_curso.html", context)


def projeto_view(request):
    context = {
        'projetos': Projeto.objects.all().order_by('nome'),
    }
    return render(request, "curso/projeto.html", context)

def detalhes_disciplina_view(request, disciplina_id):
    context= {
        'disciplina': Disciplina.objects.get(id=disciplina_id),
    }

    return render(request, 'curso/disciplina.html',context)


@login_required
def novo_curso_view(request):

    form = CursoForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('curso:curso')

    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)



@login_required
def edita_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)

    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:curso')
    else:
        form = CursoForm(instance=curso)

    context = {'form': form, 'curso':curso}
    return render(request, 'curso/edita_curso.html', context)




@login_required
def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('curso:curso')



@login_required
def nova_disciplina_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    form = DisciplinaForm(request.POST or None, request.FILES)

    if form.is_valid():
        disciplina = form.save(commit=False)
        disciplina.cursos = curso
        disciplina.save()
        return redirect('curso:disciplina')

    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'curso/nova_disciplina.html', context)


@login_required
def edita_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina', disciplina_id=disciplina.id)
    else:
        form = DisciplinaForm(instance=disciplina)

    context = {'form': form, 'disciplina': disciplina}
    return render(request, 'curso/edita_disciplina.html', context)



@login_required
def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    disciplina.delete()
    return redirect('curso:disciplina')

@login_required
def disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    context = {'disciplina': disciplina}
    return render(request, 'curso/disciplina.html', context)



@login_required
def novo_projeto_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    form = ProjetoForm(request.POST or None, request.FILES)

    if form.is_valid():
        projeto = form.save(commit=False)
        projeto.disciplinas = disciplina
        disciplina.save()
        return redirect('curso:projeto')

    context = {'form': form}
    return render(request, 'curso/novo_projeto.html', context)



@login_required
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            # Corrigindo o redirecionamento para a visualização da disciplina
            return redirect('curso:disciplina', disciplina_id=projeto.disciplinas.first().id)
    else:
        form = ProjetoForm(instance=projeto)

    context = {'form': form, 'projeto': projeto}
    return render(request, 'curso/edita_projeto.html', context)




@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('curso:projeto')




