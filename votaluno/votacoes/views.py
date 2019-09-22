from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Aluno
@login_required
def home(request):
  alunos = Aluno.objects
    return render(request, 'home.html')
def admin(request):
  return HttpResponseRedirect('/admin')