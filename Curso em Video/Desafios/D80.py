lista = []
for c in range(0, 5):
    valores = int(input(f'Digite um valor: '))
    if len(lista) == 0 or valores > max(lista):
        lista.append(valores)
        print(f'Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                lista.insert(pos, valores)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')