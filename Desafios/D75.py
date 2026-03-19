par = 0
num = []
for c in range (0, 4):
    valor = int(input('Digite um número: '))
    num.append(valor)
    if valor % 2 == 0:
        par += 1
valores = tuple(num)
print (f'O número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print (f'O primeiro número 3 foi digitado na posição {valores.index(3)+1}.')
else:
    print ('O número 3 não foi digitado.')
print(f'Foram digitados {par} números pares.')