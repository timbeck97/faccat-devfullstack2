from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidatos, name='candidatos'),
    path('candidatos/<int:id>/', views.detalhar_candidato, name='detalhar_candidato'),
    path('vagas/<int:id>/', views.detalhar_vaga, name='detalhar_vaga'),
    path('novo_candidato/', views.novo_candidato, name='novo_candidato'),
    path('nova_vaga/', views.nova_vaga, name='nova_vaga'),
]
