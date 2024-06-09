from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="bandas/", null=True, blank=True, default=None)
    nacionalidade = models.CharField(max_length=255)
    ano_de_criacao = models.IntegerField(default=None)
    detalhe = models.CharField(max_length=255, null=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to="bandas", null=True, blank=True, default=None)
    #ficheiro = models.FileField(upload_to='bandas/ficheiros', null=True, blank=True)
    ano_lancamento = models.IntegerField(default=None)


    def __str__(self):
        return self.titulo

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    data = models.DateField(auto_now_add=True)
    spotify_link = models.URLField(blank=True)
    duracao = models.DurationField()
    letra = models.TextField(default='', null=True, blank=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.titulo
