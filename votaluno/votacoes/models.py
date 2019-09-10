from django.db import models

class Turma(models.Model):
    Curso = models.TextField(max_length=30)
    Ano = models.IntegerField()
    Sala = models.TextField(max_length=1)

    def __str__(self):
        return f'{self.Ano}º "{self.Sala}" {self.Curso}'