from django.db import models
from django.contrib.auth.models import User

class Turma(models.Model):
    curso = models.TextField(max_length=30)
    ano = models.IntegerField()
    sala = models.TextField(max_length=1)

    def __str__(self):
        return f'{self.ano}º "{self.sala}" {self.curso}'

class Aluno(models.Model):
    nome = models.TextField(max_length=50)
    cpf = models.TextField(max_length=14)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class AvaliacaoAluno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    bimestre = models.IntegerField()
    #ano
    
    class Meta:
        verbose_name = 'Avaliação de aluno'
        verbose_name_plural = 'Avaliações de alunos'

    def __str__(self):
        return f'{self.aluno} - {self.usuario}'
    
class AvaliacaoTurma(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE)
    bimestre = models.IntegerField()
    #ano
    
    class Meta:
        verbose_name = 'Avaliação de turma'
        verbose_name_plural = 'Avaliações de turmas'

    def __str__(self):
        return f'{self.aluno} - {self.usuario}'
    
class Conselho(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateField(auto_now=False)
    situacao = models.BooleanField(default=False)
    
    def __str__(self):
        return self.turma

class Votacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    situacao = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Votação'
        verbose_name_plural = 'Votações'

class Voto(models.Model):
    SITUACAO_CHOICES={
        ('Aprovar', 'Aprovar'),   
        ('Reprovar', 'Reprovar'),   
        ('Abster', 'Abster')
    }
    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=8, choices=SITUACAO_CHOICES, default='Abster')