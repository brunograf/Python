s = 0
for c in range (1, 500):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print (f'A soma de todos os números impares multiplos de 3 entre 1 e 500 é {s}')