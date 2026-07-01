num = []

def sorteia(num):
    from random import randint
    for c in range(0, 5):
        num.append(randint(0, 10))
    print(f'Os valores sorteados foram: {num}')

def somaPar(num):
    s = 0
    for c in num:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {num}, temos {s}')


sorteia(num)
somaPar(num)