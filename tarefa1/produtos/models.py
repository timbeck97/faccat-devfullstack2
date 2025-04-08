from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
 
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    descricao = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    