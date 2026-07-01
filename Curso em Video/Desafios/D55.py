maior = 0
menor = 100
for c in range (0, 5):
    peso = float(input('Digite o peso do aluno (kg): '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso foi {maior} kg e o menor peso foi {menor} kg.')