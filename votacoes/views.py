from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Aluno, AvaliacaoTurma, AvaliacaoAluno, Turma, OfertaDisciplina, Conselho,UsuarioConselho, Votacao, Voto
from django.shortcuts import render, redirect
from datetime import datetime
from .avaliacoes import *

@login_required
def home(request):
  context = {}
  conselhos_professor=[]
  conselhos_abertos = []
  conselhos = request.user.conselhos_usuario.all()
  for conselho in conselhos:
    conselhos_professor.append(conselho.conselho)
  for conselho in Conselho.objects.filter(situacao=True):
    if conselho in conselhos_professor:
      conselhos_abertos.append(conselho)
  print(conselhos)
  print(conselhos_abertos)
  print(conselhos_professor)
  context['conselhos_abertos'] = conselhos_abertos
  return render(request, 'home.html',context)

# Views que manipulam as avaliações das turmas
@login_required
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

@login_required
def criarAvaliacaoTurma(request, avaliacao_id):
  context = {}
  avaliacao = AvaliacaoTurma.objects.get(id=avaliacao_id)
  context['avaliacao'] = avaliacao
  context['opcoes'] = DICT_TURMA
  return render(request,'avaliacoes/avaliarTurma.html', context)

@login_required
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

@login_required
def visualizarAvaliacaoTurma(request, avaliacao_id):
  context = {}
  avaliacao = AvaliacaoTurma.objects.get(id=avaliacao_id)
  context['avaliacao'] = avaliacao
  context['opcoes'] = get_array_turma(avaliacao.avaliacao)
  return render(request,'avaliacoes/visualizarAvaliacaoTurma.html', context)

#Views que manipulam as avaliações dos alunos
@login_required
def gerarAvaliacoesTurma(request):
  turma = Turma.objects.get(id=request.POST.get("turma"))  
  bimestre = request.POST.get("bimestre")
  alunos = Aluno.objects.filter(turma=turma)
  ofertaDisciplinas_turma = OfertaDisciplina.objects.filter(turma=turma)
  for disciplina in ofertaDisciplinas_turma:
    avaliacaoTurma =  AvaliacaoTurma(oferta_disciplina=disciplina,bimestre=bimestre,ano=int(datetime.now().year))
    avaliacaoTurma.save()
    for aluno in alunos:
      avaliacaoAluno = AvaliacaoAluno(oferta_disciplina=disciplina,aluno=aluno,bimestre=bimestre,ano=int(datetime.now().year))
      avaliacaoAluno.save()
  return administracao(request)

@login_required
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

@login_required
def criarAvaliacaoAluno(request, avaliacao_id):
  context = {}
  avaliacao = AvaliacaoAluno.objects.get(id=avaliacao_id)
  context['avaliacao'] = avaliacao
  context['opcoes'] = DICT_ALUNO
  return render(request,'avaliacoes/avaliarAluno.html', context)

@login_required
def lancarAvaliacaoAluno(request, avaliacao_id):
  soma = 0
  selecionadas = request.POST.getlist('checks')
  for opcao in selecionadas:
    soma += int(opcao)
  avaliacao = AvaliacaoAluno.objects.get(pk=avaliacao_id)
  avaliacao.status = False
  avaliacao.avaliacao = soma
  avaliacao.outros_avaliacao = request.POST.get('outros')
  avaliacao.save()
  return avaliacoesAlunos(request)

@login_required
def visualizarAvaliacaoAluno(request, avaliacao_id):
  context = {}
  avaliacao = AvaliacaoAluno.objects.get(id=avaliacao_id)
  context['avaliacao'] = avaliacao
  context['opcoes'] = get_array_aluno(avaliacao.avaliacao)
  return render(request,'avaliacoes/visualizarAvaliacaoAluno.html', context)

#Views que manipulam a administração
@login_required
def administracao(request):
  context = {}
  turmas = Turma.objects.all
  conselhosFechados = Conselho.objects.filter(situacao=False)
  conselhosAbertos = Conselho.objects.filter(situacao=True)
  context['turmas'] = turmas
  context['conselhosFechados'] = conselhosFechados
  context['conselhosAbertos'] = conselhosAbertos
  return render(request,'administracao.html', context)

@login_required
def admin(request):
  return HttpResponseRedirect('/admin')

#Views para Conselhos
@login_required
def gerarConselho(request):
  # Gerar conselho
  turma = Turma.objects.get(id=request.POST.get("turma"))  
  data = request.POST.get("data")
  conselho = Conselho.objects.create(
    turma= turma,
    data= data,
    situacao = False,
  )
  conselho.save()
  #Criar e popular lista de professores que dão aula para essa turma
  professores = []
  for disciplina in turma.disciplinas_turma.all():
    if not disciplina.professor in professores:
      professores.append(disciplina.professor)

  # Gerar relacionamento UsuarioConselho
  if professores:
    print(professores)
    for professor in professores:
      usuario_conselho = UsuarioConselho(usuario=professor,conselho=conselho)
      usuario_conselho.save()
  # Gerar votacoes dos alunos da turma deste conselho
  alunos = Aluno.objects.filter(turma=turma)
  for aluno in alunos:
    votacao_aluno = Votacao(aluno=aluno,conselho=conselho)
    votacao_aluno.save()
    #Gerar votos em branco para os professores deste conselho
    for professor in professores:
      voto_branco = Voto(usuario=professor,votacao=votacao_aluno)
      voto_branco.save()

  return administracao(request)

@login_required
def iniciarConselho(request):
  # Pesquisar e iniciar o conselho
  conselho_id = request.POST.get("conselho")
  conselho = Conselho.objects.get(id=conselho_id)
  conselho.situacao = True
  conselho.save()
  # Pesquisar e iniciar as votações dos alunos que pertencem à turma deste conselho
  alunos = Aluno.objects.filter(turma=conselho.turma)
  for aluno in alunos:
    votacao_aluno = Votacao.objects.get(aluno=aluno,conselho=conselho)
    votacao_aluno.situacao = True
    votacao_aluno.save()

  return administracao(request)
  

@login_required
def encerrrarConselho(request):
  # Pesquisar e encerrar o conselho
  conselho_id = request.POST.get("select")
  conselho = Conselho.objects.get(id=conselho_id)
  conselho.situacao = False
  conselho.save()
  # Pesquisar e encerrar as votações dos alunos que pertencem à turma deste conselho
  alunos = Aluno.objects.filter(turma=conselho.turma)
  for aluno in alunos:
    votacao_aluno = Votacao.objects.get(aluno=aluno,conselho=conselho)
    votacao_aluno.situacao = False
    votacao_aluno.save()
  return administracao(request)

#erros
def error404(request,exception):
  return render(request, '404.html', status=404)

def error500(request):
  return render(request, '500.html', status=500)