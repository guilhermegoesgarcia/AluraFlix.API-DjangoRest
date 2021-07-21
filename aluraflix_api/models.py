from django.db import models

# Create your models here.
# Criando Base de dados

class videos (models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo, self.descricao, self.url