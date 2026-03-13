from datetime import date
maior = 0
menor = 0
for c in range (0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade.\nE {menor} pessoas são menores de idade.')
