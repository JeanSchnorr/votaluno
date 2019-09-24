from django.contrib import admin
from .models import Turma, Aluno, Votacao,Voto,AvaliacaoAluno,AvaliacaoTurma,Conselho,OfertaDisciplina,Curso,Disciplina

admin.site.register(Turma);
admin.site.register(Aluno);
admin.site.register(Conselho);
admin.site.register(AvaliacaoAluno);
admin.site.register(AvaliacaoTurma);
admin.site.register(Votacao);
admin.site.register(Voto);
admin.site.register(Disciplina);
admin.site.register(OfertaDisciplina);
admin.site.register(Curso);