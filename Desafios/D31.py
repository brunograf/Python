km = float(input('Qual é a distância (km) da sua viagem? '))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(f'O preço da sua viagem é R${preco:.2f}.')