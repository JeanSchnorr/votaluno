from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Aluno, AvaliacaoTurma, Turma, OfertaDisciplina
from django.shortcuts import render, redirect
from .avaliacoes import *

@login_required
def home(request):
  return render(request, 'home.html')

def avaliacoesTurmas(request):
  context = {}
  avaliacoes=[]
  ofertas = OfertaDisciplina.objects.filter(professor=request.user)

  for oferta in ofertas:
    avs = AvaliacaoTurma.objects.filter(oferta_disciplina=oferta).filter(status=True)
    if len(avs) > 0:
      for avaliacoesDisciplina in avs:
        avaliacoes.append(avaliacoesDisciplina)

  context['avaliacoes'] = avaliacoes
  return render(request,'avaliacoes/avaliacoesTurmas.html',context)

def criarAvaliacaoTurma(request, avaliacao_id):
  context = {}
  avaliacao = AvaliacaoTurma.objects.get(id=avaliacao_id)
  context['avaliacao'] = avaliacao
  context['opcoes'] = DICT_TURMA
  return render(request,'avaliacoes/avaliarTurma.html', context)

def lancarAvaliacaoTurma(request, avaliacao_id):
  soma = 0
  selecionadas = request.POST.getlist('checks')
  for opcao in selecionadas:
    soma += int(opcao)
  avaliacao = AvaliacaoTurma.objects.get(pk=avaliacao_id)
  avaliacao.status = False
  avaliacao.avaliacao = soma
  avaliacao.save()
  return avaliacoesTurmas(request)

def admin(request):
  return HttpResponseRedirect('/admin')