from django.db import models
from django.contrib.auth.models import User

CHOICES_BIMESTRE=[(1,'1'),(2,'2'),(3,'3'),(4,'4')]

class Disciplina(models.Model):
    nome = models.TextField(max_length=30)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.TextField(max_length=30)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ano = models.IntegerField()
    sala = models.TextField(max_length=1)

    def __str__(self):
        return f'{self.ano}º "{self.sala}" {self.curso}'

class OfertaDisciplina(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.disciplina} - {self.professor}'

class Aluno(models.Model):
    nome = models.TextField(max_length=50)
    cpf = models.TextField(max_length=14)
    foto = models.ImageField(default='default.png',upload_to='alunos/')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class AvaliacaoAluno(models.Model):
    oferta_disciplina = models.ForeignKey(OfertaDisciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    bimestre = models.PositiveIntegerField(choices=CHOICES_BIMESTRE)
    avaliacao = models.PositiveIntegerField(default=0)
    outros_avaliacao = models.TextField(max_length=255,blank=True,null=True)
    ano = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
        
    class Meta:
        verbose_name = 'Avaliação de aluno'
        verbose_name_plural = 'Avaliações de alunos'

    def __str__(self):
        return f'{self.aluno} - {self.oferta_disciplina}'
    
class AvaliacaoTurma(models.Model):
    oferta_disciplina = models.ForeignKey(OfertaDisciplina, on_delete=models.CASCADE)
    bimestre = models.PositiveIntegerField(choices=CHOICES_BIMESTRE)
    ano = models.PositiveIntegerField()
    avaliacao = models.PositiveIntegerField(default=0)
    outros_avaliacao = models.TextField(max_length=255,blank=True,null=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Avaliação de turma'
        verbose_name_plural = 'Avaliações de turmas'

    def __str__(self):
        return f'{self.oferta_disciplina.turma} - {self.oferta_disciplina} - {self.ano}'
    
class Conselho(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateField(auto_now=False)
    situacao = models.BooleanField(default=False)
    
    def __str__(self):
        if self.situacao:
            text = 'Iniciada'
        else:
            text = 'Fechada'
        return f'{self.turma} - {text}'

class UsuarioConselho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conselho = models.ForeignKey(Conselho, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario} - {self.conselho}'

class Votacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    situacao = models.BooleanField(default=False)
    conselho = models.ForeignKey(Conselho, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Votação'
        verbose_name_plural = 'Votações'

    def __str__(self):
        return f'{self.aluno} - {self.conselho.turma}'


class Voto(models.Model):
    SITUACAO_CHOICES={
        ('Aprovar', 'Aprovar'),   
        ('Reprovar', 'Reprovar'),   
        ('Abster', 'Abster')
    }
    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=8, choices=SITUACAO_CHOICES, default='Abster')

    def __str__(self):
        return f'{self.usuario} para {self.votacao}'
