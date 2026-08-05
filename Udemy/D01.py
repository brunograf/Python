def encontra_duplicados(lista):
    """
    Função que recebe uma lista e retorna o primeiro elemento duplicado. Se nenhuma duplicação for encontrada, retorna um aviso.
    """
    for n in lista:
        if lista.count(n) > 1:
            return n
    return 'Nenhum elemento duplicado encontrado'


lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 8, 7, 3, 9, 5, 6, 10],
    [1, 9, 10, 3, 7, 4, 7, 1, 8, 9]
]

for lista in lista_de_listas_de_inteiros:
    duplicado = encontra_duplicados(lista)
    print(f'Lista: {lista}')
    print(f'Primeiro elemento duplicado: {duplicado}')
    print()