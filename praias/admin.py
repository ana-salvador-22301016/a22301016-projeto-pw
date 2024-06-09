from django.contrib import admin

# Register your models here.
from .models import Praia
from .models import Regiao
from .models import Servico

admin.site.register(Praia)
admin.site.register(Regiao)
admin.site.register(Servico)
