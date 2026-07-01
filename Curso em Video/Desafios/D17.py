from math import hypot
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)
print(f'A hipotenusa vale {hipotenusa:.2f}')