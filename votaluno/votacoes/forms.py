from django import forms
from .models import AvaliacaoTurma

class AvaliacaoTurmaForm(forms.Form):
    avaliacoes = AvaliacaoTurma.objects.filter(usuario=request.user)[:10]

