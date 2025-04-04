from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico, Consulta
from .formulario import Formulario_consulta

def base(request):
    return render(request, 'base.html')

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        formulario = Formulario_consulta(request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = Formulario_consulta()
    return render(request, 'form_consulta.html', {'formulario': formulario})

def detalhes_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'detalhes_consulta.html', {'consulta': consulta})