from random import randint
num_aleatorio = randint(0, 10)
num_escolhido = int(input('Pensei num número entre 0 e 10. Tente adivinhar: '))
c = 0
while num_escolhido != num_aleatorio:
    num_escolhido = int(input('Que pena! Tente novamente: '))
    c += 1
print(f'Parabéns! Vocé acertou o número em {c} tentativas!')