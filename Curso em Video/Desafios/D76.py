listagem = ('Pão', 1.99, 'Leite', 2.50, 'Tomate', 4.20, 'Alface', 4.90, 'Arroz', 6.50, 'Feijão', 7.80)
print('=========Listagem de Preços=========')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')