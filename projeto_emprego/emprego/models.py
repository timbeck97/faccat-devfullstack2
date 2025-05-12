from django.db import models

# Create your models here.
GENERO = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]
ESCOLARIDADE = [
    ('ENSINO_FUNDAMENTAL','Ensino Fundamental'),
    ('ENSINO_MEDIO','Ensino Médio'),
    ('CURSO_TECNICO', 'Curso Técnico'),
    ('CURSO_SUPERIOR', 'Curso Superior')
]
AREA = [
    ('DESENVOLVEDOR', 'Desenvolvedor'),
    ('QA','Tester'),
    ('LIDER', 'Lider Técnico')
]
CONTRATO = [
    ('PJ', 'Pessoa Júrídica'),
    ('CLT', 'CLT')
]

class Vaga(models.Model):
    titulo = models.CharField(max_length=50)
    area = models.CharField(max_length=15, choices=AREA)
    tipo_contrato = models.CharField(max_length=15, choices=CONTRATO)
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return self.titulo
        
class Candidato(models.Model):
  
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO)
    email = models.CharField(max_length=50)
    escolaridade = models.CharField(max_length=50, choices=ESCOLARIDADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
        
