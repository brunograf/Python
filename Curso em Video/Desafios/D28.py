import random
num_aleatorio = random.randint(0, 5)
num_escolhido = int(input('Pensei num número entre 0 e 5. Tente adivinhar: '))
if num_escolhido == num_aleatorio:
    print('Parabéns! Você acertou o número!')
else:
    print(f'Que pena! O número correto era {num_aleatorio}.')