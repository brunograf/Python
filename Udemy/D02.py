def unir_listas(lista1, lista2):
    """
    Une duas listas combinando os elementos correspondentes de `lista1` e `lista2` com um separador de ' - '.

    Parâmetros:
        lista1 (list): A primeira lista.
        lista2 (list): A segunda lista.

    Retorna:
        list: Uma nova lista com os elementos combinados.
    """
    try:
        return [f'{lista1[i]} - {lista2[i]}' for i in range(len(lista2))]
    except IndexError:
        return [f'{lista1[i]} - {lista2[i]}' for i in range(len(lista1))]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
lista_unida = unir_listas(cidades, estados)
print(lista_unida)