from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Aluno, AvaliacaoTurma, Turma, OfertaDisciplina
from django.shortcuts import render, redirect
from .avaliacoes import *

@login_required
def home(request):
  return render(request, 'home.html')

# Views que manipulam as avaliações das turmas
def avaliacoesTurmas(request):
  context = {}
  avaliacoes=[]
  avaliacoes_lancadas=[]
  ofertas = OfertaDisciplina.objects.filter(professor=request.user)
  for oferta in ofertas:
    avs = AvaliacaoTurma.objects.filter(oferta_disciplina=oferta).filter(status=True)
    avs_lancadas = AvaliacaoTurma.objects.filter(oferta_disciplina=oferta).filter(status=False)[:10]
    if len(avs_lancadas) > 0:
      for avaliacoesLancadas in avs_lancadas:
        avaliacoes_lancadas.append(avaliacoesLancadas)

    if len(avs) > 0:
      for avaliacoesDisciplina in avs:
        avaliacoes.append(avaliacoesDisciplina)

  context['avaliacoes'] = avaliacoes
  context['avaliacoes_lancadas'] = avaliacoes_lancadas
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
  avaliacao.outros_avaliacao = request.POST.get('outros')
  avaliacao.save()
  return avaliacoesTurmas(request)

def visualizarAvaliacaoTurma(request, avaliacao_id):
  context = {}
  avaliacao = AvaliacaoTurma.objects.get(id=avaliacao_id)
  context['avaliacao'] = avaliacao
  context['opcoes'] = get_array_turma(avaliacao.avaliacao)
  return render(request,'avaliacoes/visualizarAvaliacaoTurma.html', context)

#Views que manipulam as avaliações dos alunos
def avaliacoesAlunos(request):
  context = {}
  avaliacoes=[]
  avaliacoes_lancadas=[]
  ofertas = OfertaDisciplina.objects.filter(professor=request.user)
  for oferta in ofertas:
    avs = AvaliacaoAluno.objects.filter(oferta_disciplina=oferta).filter(status=True)
    avs_lancadas = AvaliacaoAluno.objects.filter(oferta_disciplina=oferta).filter(status=False)[:10]
    if len(avs_lancadas) > 0:
      for avaliacoesLancadas in avs_lancadas:
        avaliacoes_lancadas.append(avaliacoesLancadas)

    if len(avs) > 0:
      for avaliacoesDisciplina in avs:
        avaliacoes.append(avaliacoesDisciplina)

  context['avaliacoes'] = avaliacoes
  context['avaliacoes_lancadas'] = avaliacoes_lancadas
  return render(request,'avaliacoes/avaliacoesAlunos.html',context)
def admin(request):
  return HttpResponseRedirect('/admin')