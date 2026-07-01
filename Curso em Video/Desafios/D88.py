from random import randint
from time import sleep
print('=-' * 30)
print('JOGO DA MEGA SENA')
print('=-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
jogo = []
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    print(f'Jogo {tot}: {jogo}')
    sleep(1)
    jogo.clear()
    tot += 1
print('=-' * 30)
print('BOA SORTE!')