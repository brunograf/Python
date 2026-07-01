num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
c = num
while c > 1:
    fatorial *= c
    c -= 1
print(f'O fatorial de {num} é {fatorial}')