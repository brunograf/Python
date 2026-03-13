primeiro = int(input('Digite o 1º termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
for c in range(primeiro, primeiro + 10 * razao, razao):
    print(f'{c} ')
print('FIM')