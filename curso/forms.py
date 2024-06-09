from django import forms    # formulários Django
from .models import Curso
from .models import Disciplina
from .models import Projeto


class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = '__all__'



class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina
    fields = '__all__'


class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = '__all__'


