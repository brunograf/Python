jogador = {}
time = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    jogador['total'] = 0
    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jogador['total'] += jogador['gols'][c]
    time.append(jogador.copy())
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"GOLS":>8}{"TOTAL":>8}')
print('-' * 26)
for i, jogador in enumerate(time):
    print(f'{i:<4}{jogador["nome"]:<10}{str(jogador["gols"]):<15}{jogador["total"]:<8}')
print('-' * 26)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if opc == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {time[opc]["nome"]}:')
    for c, v in enumerate(time[opc]['gols']):
        print(f'    => Na partida {c + 1}, fez {v} gols.')
    print(f'Foi um total de {time[opc]["total"]} gols.')
    print('-' * 26)