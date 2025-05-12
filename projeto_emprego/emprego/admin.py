from django.contrib import admin
from .models import Candidato, Vaga
# Register your models here.
@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'area', 'tipo_contrato')
    list_filter = ('area', 'tipo_contrato')
    search_fields = ('titulo',)

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'genero', 'escolaridade', 'vaga')
    list_filter = ('genero', 'escolaridade', 'vaga')
    search_fields = ('nome', 'sobrenome', 'email')