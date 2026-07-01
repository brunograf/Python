num = 0
soma = 0
continuar = 'S'
c = 0
maior = 0
menor = 100
while continuar == 'S':
    c += 1
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
media = soma / c
print(f'A média dos números digitados é {media:.2f}')
print(f'O maior número digitado foi {maior}')
print(f'E o menor número digitado foi {menor}')