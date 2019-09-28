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
  avaliacoes=[]
  ofertas = OfertaDisciplina.objects.filter(professor=request.user)
  for oferta in ofertas:
    avaliacoesDisciplina = AvaliacaoTurma.objects.filter(oferta_disciplina=oferta).filter(status=True)[0]
    avaliacoes.append(avaliacoesDisciplina)

  context['avaliacoes'] = avaliacoes
  return render(request,'avaliacoes/avaliacoesTurmas.html',context)

def criarAvaliacaoTurma(request,avaliacao_id):
  context = {}
  avaliacao = AvaliacaoTurma.objects.get(avaliacaoTurma.id=avaliacao_id)
  return render(request,'avaliacoes/avaliarTurma.html')

def admin(request):
  return HttpResponseRedirect('/admin')