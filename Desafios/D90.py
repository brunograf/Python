boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['media'] >= 7:
    boletim['situacao'] = 'aprovado'
elif 5 <= boletim['media'] < 7:
    boletim['situacao'] = 'em recuperação'
else:
    boletim['situacao'] = 'reprovado'
print(f'O aluno {boletim["nome"]} têm a média {boletim["media"]} e está {boletim["situacao"]}')