n = int (input ('Escolha um número para ver a tabuada: '))
print (f'====== TABUADA DE {n} =======')
for c in range (1, 11):
    print (f'{n} x {c} = {n*c}')