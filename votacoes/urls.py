from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('AvaliacoesTurmas/', views.avaliacoesTurmas, name='avaliacoesTurmas'),
    path('AvaliacoesTurmas/<int:avaliacao_id>', views.criarAvaliacaoTurma, name='criarAvaliacaoTurma'),
    path('AvaliacoesTurmas/<int:avaliacao_id>/salvar', views.lancarAvaliacaoTurma, name='lancarAvaliacaoTurma'),
    path('AvaliacoesTurmas/<int:avaliacao_id>/visualizar', views.visualizarAvaliacaoTurma,  name='visualizarAvaliacaoTurma'),
    path('AvaliacoesAlunos/', views.avaliacoesAlunos, name='avaliacoesAlunos'),
    path('AvaliacoesAlunos/<int:avaliacao_id>', views.criarAvaliacaoAluno, name='criarAvaliacaoAluno'),
    path('AvaliacoesAlunos/<int:avaliacao_id>/salvar', views.lancarAvaliacaoAluno, name='lancarAvaliacaoAluno'), 
    path('AvaliacoesAlunos/<int:avaliacao_id>/visualizar', views.visualizarAvaliacaoAluno,  name='visualizarAvaliacaoAluno'),
    path('Administracao', views.administracao,  name='administracao'),
    path('Administracao/gerarAvaliacoesTurma', views.gerarAvaliacoesTurma,  name='gerarAvaliacoesTurma'),
    path('Administracao/gerarConselho', views.gerarConselho,  name='gerarConselho'),
    path('Administracao/iniciarConselho', views.iniciarConselho,  name='iniciarConselho'),
    path('Administracao/encerrrarConselho', views.encerrrarConselho,  name='encerrrarConselho'),
    path('Administracao/exibirConselho/<int:conselho_id>', views.exibirConselho,  name='exibirConselho'),
    path('exibirConselho/<int:conselho_id>', views.exibirConselho,  name='exibirConselho'),
    path('votar/<int:conselho_id>/<int:aluno_id>', views.exibirVoto,  name='exibirVoto'),
    path('votar/lancandoVoto/<int:conselho_id>', views.lancarVoto,  name='lancarVoto'),
]
