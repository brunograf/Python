jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
jogador['total'] = 0
for c in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['total'] += jogador['gols'][c]
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c, v in enumerate(jogador['gols']):
    print(f'    => Na partida {c + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')