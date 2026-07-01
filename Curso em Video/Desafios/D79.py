valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    if valores[-1] in valores[:-1]:
        print('Valor duplicado! Não vou adicionar...')
        valores.pop()
    else:
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
valores.sort()
print(f'Voce digitou os valores {valores}')