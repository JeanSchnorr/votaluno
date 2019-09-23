from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Aluno, AvaliacaoTurma, Turma
from django.shortcuts import render

@login_required
def home(request):
  return render(request, 'home.html')

def avaliacoesTurmas(request):
  context = {}
  turmas = Turma.objects.filter()
  avaliacoes = AvaliacaoTurma.objects.filter(usuario=request.user)[:10]
  context['avaliacoes'] = avaliacoes
  return render(request,'avaliacoes/avaliacoesTurmas.html',context)

def criarAvaliacaoTurma(request):
  return redirect('avaliacoes/avaliacoesTurmas.html')

def admin(request):
  return HttpResponseRedirect('/admin')