from itertools import groupby

alunos = [
    {'nome': 'Bruno', 'nota': 'A'},
    {'nome': 'Juju', 'nota': 'B'},
    {'nome': 'Alice', 'nota': 'A'},
    {'nome': 'Lucas', 'nota': 'C'},
    {'nome': 'Maíra', 'nota': 'B'},
    {'nome': 'Willy', 'nota': 'D'}
]

alunos.sort(key=lambda aluno: aluno['nota'])

for nota, alunos in groupby(alunos, key=lambda aluno: aluno['nota']):
    print(f'Nota {nota}:')
    for aluno in alunos:
        print(f'    {aluno["nome"]}')