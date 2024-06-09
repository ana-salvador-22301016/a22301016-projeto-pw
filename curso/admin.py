from django.contrib import admin

# Register your models here.
from .models import Curso
from .models import Disciplina
from .models import Area_cientifica
from .models import Projeto
from .models import Linguagem
from .models import Docente

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Area_cientifica)
admin.site.register(Projeto)
admin.site.register(Linguagem)
admin.site.register(Docente)
