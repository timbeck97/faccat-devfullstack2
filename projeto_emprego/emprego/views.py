from django.shortcuts import render,redirect
from .models import Candidato, Vaga
from .forms import CandidatoForm, VagaForm
# Create your views here.
def candidatos(request):
    candidatos = Candidato.objects.all()
    resp = {
        'candidatos' : candidatos
    }
    return render(request, 'emprego/candidatos.html', resp)
def detalhar_candidato(request, id):
    candidato = Candidato.objects.get(id=id)
    resp = {
        'candidato' : candidato
    }
    return render(request, 'emprego/detalhar_candidato.html', resp)
def detalhar_vaga(request, id):
    vaga = Vaga.objects.get(id=id)
    resp = {
        'vaga' : vaga
    }
    return render(request, 'emprego/detalhar_vaga.html', resp)

def novo_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidatos') 
    else:
        form = CandidatoForm()

    return render(request, 'emprego/novo_candidato.html', {'form': form})

def nova_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidatos') 
    else:
        form = VagaForm()

    return render(request, 'emprego/nova_vaga.html', {'form': form})
