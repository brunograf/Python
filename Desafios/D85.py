valores = [[], []]
for c in range (0, 8):
    num = int(input(f'Digite o {c + 1}° número: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]}')
print(f'E os ímpares digitados foram {valores[1]}')