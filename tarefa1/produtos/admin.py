from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
@admin.register(Produto)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco","descricao","categoria")
    list_filter =  ("categoria",)