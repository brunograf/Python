matriz = [[], [], []]
pares = 0
terceiracol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            terceiracol += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares digitados é {pares}')
print(f'A soma dos valores da terceira coluna é {terceiracol}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')