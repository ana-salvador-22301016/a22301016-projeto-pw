from django.db import models

# Create your models here.

class Curso(models.Model):
    nome= models.CharField(max_length= 100)
    apresentacao= models.CharField(max_length= 500)
    objetivo= models.CharField(max_length= 255)
    competencia= models.CharField(max_length= 255)


    def __str__(self):
         return self.nome


class Area_cientifica(models.Model):
    nome= models.CharField(max_length= 100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length= 100)
    ano = models.IntegerField(default=None)
    semestre = models.CharField(max_length= 100)
    ects = models.IntegerField(default=None)
    curricularIUnitReadableCode= models.CharField(max_length= 255)
    areaCientifica= models.ForeignKey(Area_cientifica, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso, related_name="disciplinas")



    def __str__(self):
        return self.nome




class Projeto(models.Model):
    nome= models.CharField(max_length= 100)
    descricao= models.CharField(max_length= 255)
    conceitoAplicado= models.CharField(max_length= 255)
    tecnologiaUtilizada= models.CharField(max_length= 100)
    linkYoutube= models.URLField(blank=True)
    linkGitHub= models.URLField(blank=True)
    imagem= models.ImageField(upload_to="curso", null=True, blank=True, default=None)
    disciplinas = models.ManyToManyField(Disciplina, related_name="projetos")


    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome= models.CharField(max_length= 100)
    disciplina= models.ManyToManyField(Disciplina )


    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='', blank=True)
    disciplinas = models.ManyToManyField(Disciplina, related_name="docentes")


    def __str__(self):

        return self.nome

