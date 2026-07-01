primeiro = int(input('Digite o 1º termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
c = 0
while c < 10:
    print(f'{primeiro + razao * c}')
    c += 1
print('FIM')