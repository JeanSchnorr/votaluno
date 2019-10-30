from django.contrib import admin
from .models import *

admin.site.register(Turma);
admin.site.register(Aluno);
admin.site.register(Conselho);
admin.site.register(UsuarioConselho);
admin.site.register(AvaliacaoAluno);
admin.site.register(AvaliacaoTurma);
admin.site.register(Votacao);
admin.site.register(Voto);
admin.site.register(Disciplina);
admin.site.register(OfertaDisciplina);
admin.site.register(Curso);