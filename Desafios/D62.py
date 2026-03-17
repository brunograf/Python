primeiro = int(input('Digite o 1º termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
c = 0
while c < 10:
    print(f'{primeiro + razao * c}')
    c += 1
c = int(input('Quantos termos vocé quer mostrar a mais? '))
while c != 0:
    for c in range(0, c):
        print(f'{primeiro + razao * (c + 10)}')
    c = int(input('Quantos termos vocé quer mostrar a mais? '))
print('FIM')