from django.contrib import admin
from .models import Turma, Aluno, Votacao,Voto,Avaliacao,Conselho

admin.site.register(Turma);
admin.site.register(Aluno);
admin.site.register(Conselho);
admin.site.register(Avaliacao);
admin.site.register(Votacao);
admin.site.register(Voto);