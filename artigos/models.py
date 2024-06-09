from django.db import models

# Create your models here.
class Artigos(models.Model):
    autorName = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    comentario = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)

    def __str__(self):
        return f"Nome do Autor: {self.autorName} post: {self.post} comentários: {self.comentario} e rating: {self.rating} upvotes on Quora"