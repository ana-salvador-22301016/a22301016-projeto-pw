from django.db import models

# Create your models here.

class Regiao(models.Model):
    nome = models.CharField(max_length=225)


    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=225)

    def __str__(self):
        return self.nome


class Praia(models.Model):
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=225)
    servicos= models.ManyToManyField(Servico, related_name="servicos")
    foto = models.ImageField(upload_to="praias/", null=True, blank=True, default=None)
    def __str__(self):
        return self.nome
