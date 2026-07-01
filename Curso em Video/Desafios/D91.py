from random import randint
dados = {}
resultados = []
for c in range(0, 4):
    dados ['jogador'] = str(input('Nome do jogador: '))
    dados ['resultado'] = randint(1, 6)
    resultados.append(dados.copy())
print('-=' * 30)
print('Valores sorteados:')
for c in range(0, 4):
    print(f'O(A) jogador(a) {resultados[c]["jogador"]} tirou {resultados[c]["resultado"]} no dado.')
print('-=' * 30)
print('Ranking dos jogadores:')
resultados.sort(key=lambda x: x['resultado'], reverse=True)
for c in range(0, 4):
    print(f'{c + 1}° lugar: {resultados[c]["jogador"]} com {resultados[c]["resultado"]}.')

