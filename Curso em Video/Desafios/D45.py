print ('======= JOKENPÔ =======')
from random import choice
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(opcoes)
jogador = input('Escolha uma opção:\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\nOpção: ')
if jogador == '1':
    jogador = 'PEDRA'
elif jogador == '2':
    jogador = 'PAPEL'
elif jogador == '3':    
    jogador = 'TESOURA'
else:
    print('Opção inválida. Tente novamente.')
    exit()
print(f'Computador jogou: {computador}')
print(f'Você jogou: {jogador}')
if computador == jogador:
    print('Empate!')
elif jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'TESOURA' and computador == 'PAPEL':
    print('Você venceu!')
else:
    print('Computador venceu!')
