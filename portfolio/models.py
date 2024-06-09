from django.db import models

class Introduction(models.Model):
    text = models.CharField(max_length=200, verbose_name="Introduction Text")

    def __str__(self):
        return self.text

class MeByMe(models.Model):
    about = models.CharField(max_length = 500)
    interesses = models.CharField(max_length = 1000,default="EM BREVE")
    aptidoes = models.CharField(max_length=500, default="EM BREVE")
    competencias = models.CharField(max_length = 500,default="EM BREVE")
    experiencia = models.CharField(max_length = 5000,default="EM BREVE")
    cv = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.about

class TechnicalPresentation(models.Model):
    intro_text = models.TextField(max_length=2000, verbose_name="TEXTO iNTRODUTORIO")
    tech_details = models.TextField(max_length=2000, verbose_name="DETALHES")


    def __str__(self):
        return self.intro_text

class ApplicationImages(models.Model):
    bandas_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Bandas Image")
    lei_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Lei Image")
    artigos_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Artigos Image")
    meteo_image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="Meteo Image")

    def __str__(self):
        return "Application Images"

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

