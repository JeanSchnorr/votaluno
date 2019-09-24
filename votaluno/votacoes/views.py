from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Aluno, AvaliacaoTurma, Turma, OfertaDisciplina
from django.shortcuts import render

@login_required
def home(request):
  return render(request, 'home.html')

def avaliacoesTurmas(request):
  context = {}
  
  ofertasDisciplinas= OfertaDisciplina.objects.filter(professor=request.user)
  
  avaliacoes = AvaliacaoTurma.objects.filter(oferta_disciplina=ofertasDisciplinas)[:10]
  context['avaliacoes'] = avaliacoes
  return render(request,'avaliacoes/avaliacoesTurmas.html',context)

def criarAvaliacaoTurma(request):
  return redirect('avaliacoes/avaliacoesTurmas.html')

def admin(request):
  return HttpResponseRedirect('/admin')