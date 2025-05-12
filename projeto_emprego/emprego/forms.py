from django import forms
from .models import Candidato, Vaga

# Formulário para Curso
class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato 
        fields = ['nome','sobrenome','data_nascimento','genero','email','escolaridade','vaga'] 
class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga 
        fields = ['titulo','area','tipo_contrato','descricao'] 