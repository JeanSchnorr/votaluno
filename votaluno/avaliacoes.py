DICT_TURMA = {
    1: 'Participativa',
    2: 'Produtiva',
    4: 'Apática',
    8: 'Dificuldade de Relacionamento',
    16: 'Indisciplinada',
    32: 'Baixo Rendimento',
    64: 'Déficit de conteúdo',
    128: 'Outros',
}

# o mesmo que o anterior só que as chaves viram valores e os valores viram chaves
REVERSED_DICT_TURMA = dict(reversed(item) for item in DICT_TURMA.items())

DICT_ALUNO = {
    1: 'Dificuldade em aprender',
    2: 'Déficit de conteúdos',
    4: 'Faltas excessivas',
    8: 'Não realizou AVA',
    16: 'Indisciplina',
    32: 'Falta de participação',
    64: 'Não realizou atividades',
    128: 'Outros',
}

# o mesmo que o anterior só que as chaves viram valores e os valores viram chaves
REVERSED_DICT_ALUNO = dict(reversed(item) for item in DICT_ALUNO.items())

MAX_VALUE = 0xb11111111;


# recebe um inteiro e retorna um array contendo as "strings" de avaliação conforme DICT_ALUNO
# exemplo: get_array_aluno(3) deve retornar ['Dificuldade em aprender', 'Déficit de conteúdos'], isso porque três
# é a soma de 1 ('Dificuldade em aprender') + 2 ('Défict de conteúdos')
def get_array_aluno(n):
    return get_array(DICT_ALUNO, n)


# igual ao anterior mas leva em consideração o DICT_TURMA
def get_array_turma(n):
    return get_array(DICT_TURMA, n)


# função que mapeia o inteiro em valores
def get_array(d, n):
    aux = 1
    ret = []
    while aux <= MAX_VALUE:
        # bitwise AND operator
        if aux & n > 0:
            ret.append(d[aux])
        # bitwise left shift operator -> move o 1 uma casa para esquerda no binário, obtendo a seq 1, 2, 4, 8...
        aux = aux << 1
    return ret


# recebe um array com avaliações e retorna um inteiro
def array_to_int(arr, d):
    aux = 0
    for s in arr:
        aux += d[s]
    return aux


def array_to_int_aluno(arr):
    return array_to_int(arr, REVERSED_DICT_ALUNO)


def array_to_int_turma(arr):
    return array_to_int(arr, REVERSED_DICT_TURMA)


import unittest
class Test(unittest.TestCase):
    def test_aluno(self):
        arr_aluno = ['Dificuldade em aprender', 'Déficit de conteúdos', 'Faltas excessivas']
        r = array_to_int_aluno(arr_aluno)
        arr = get_array_aluno(r)
        self.assertCountEqual(arr_aluno, arr)

    def test_turma(self):
        arr_turma = ['Apática', 'Dificuldade de Relacionamento', 'Outros']
        r = array_to_int_turma(arr_turma)
        arr = get_array_turma(r)
        self.assertCountEqual(arr_turma, arr)


if __name__ == '__main__':
    unittest.main()