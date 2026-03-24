valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Os valores digitados foram {valores}')
if valores.count(max(valores)) > 1:
    print(f'Os maiores valores digitados foi {max(valores)} nas posições {valores.index(max(valores))}')
else:
    print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
if valores.count(min(valores)) > 1:
    print(f'Os menores valores digitados foi {min(valores)} nas posições {valores.index(min(valores))}')
else:
    print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')