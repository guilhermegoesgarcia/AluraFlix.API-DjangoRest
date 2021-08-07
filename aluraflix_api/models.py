from django.db import models

# Create your models here.
# Criando Base de dados

class categorias (models.Model):

    titulo = models.CharField(max_length=100, default='Sem_Categoria')
    cor = models.CharField(max_length=7)

    def __str__(self):
        return self.titulo

class videos (models.Model):
    # As regras de negocio em relação ao cadastro dos dados sáo inseridos aqui.
    titulo = models.CharField(max_length=30, default='Sem_Titulo') # os valores não podem ser nulo e nem falso
    descricao = models.CharField(max_length=150)
    url = models.CharField(max_length=100)
    categoriaId = models.ForeignKey(categorias, on_delete=models.SET_DEFAULT,default=1)

    def __str__(self):
        return self.titulo