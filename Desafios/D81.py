valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print (f'Foram digitados {len(valores)} valores')
valores.sort(reverse=True)
print (f'Os valores em ordem decrescente foram {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista e está na posição {valores.index(5)}!')
else:
    print('O valor 5 nao faz parte da lista!')