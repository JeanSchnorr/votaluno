from django import template

register = template.Library()

from django.contrib.auth.models import User
from votacoes.models import OfertaDisciplina

@register.simple_tag
def get_professores(turma):
    disciplinas = OfertaDisciplina.objects.filter(turma=turma)
    professores= []
    for disciplina in disciplinas:
        if not disciplina.professor in professores:
            professores.append(disciplina.professor)
    if professores:
        return professores
    return None