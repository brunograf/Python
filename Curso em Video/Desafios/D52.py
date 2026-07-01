print ('====== VERIFICADOR DE NÚMEROS PRIMOS =======')
num = int(input('Escolha um número para verificar: '))
for c in range (2, num):
    if num % c == 0:
        print (f'O número {num} nao é primo, pois ele é divisível por {c}.')
        break
else:
    print (f'O número {num} é primo.')