valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[-1] % 2 == 0:
        pares.append(valores[-1])
    else:
        impares.append(valores[-1])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
valores.sort()
pares.sort()
impares.sort()
print(f'Todos os valores digitados foram {valores}')
print(f'Os pares digitados foram {pares}')
print(f'E os ímpares digitados foram {impares}')