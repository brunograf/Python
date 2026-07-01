galera = []
dado = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
print ('=-' * 30)
print (f'Foram cadastradas {len(galera)} pessoas.')
print (f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print (f'[{p[0]}] ', end='')
print ()
print (f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print (f'[{p[0]}] ', end='')