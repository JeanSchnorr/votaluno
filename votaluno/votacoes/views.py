from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Aluno, AvaliacaoTurma
from django.shortcuts import render
from .forms import avalia

@login_required
def home(request):
  return render(request, 'home.html')

def avaliacoesTurmas(request):
  context = {}
  avaliacoes = AvaliacaoTurma.objects.filter(usuario=request.user)[:10]
  context['avaliacoes'] = avaliacoes
  return render(request,'avaliacoes/avaliacoesTurmas.html',context)

@require_POST
def criarAvaliacaoTurma(request):
  form = AvaliacaoTurmaForm(request.POST)
  if form.is_valid():
    novaAvaliacao = AvaliacaoTurma(usuario=request.user, turma=request.POST['Turma'],bimestre=request.POST['Bimestre'],ano=request.POST['ano'])

    novaAvaliacao.save()
  return avaliacoesTurmas

def admin(request):
  return HttpResponseRedirect('/admin')