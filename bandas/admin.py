from django.contrib import admin
# Register your models here.
from .models import Banda
from .models import Album
from .models import Musica

class BandaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album)
admin.site.register(Musica)

