def pesquisa_binaria(vetor, x, inicio, fim):
    """
    Realiza uma busca binária em uma lista ordenada para localizar um elemento.
    
    Parâmetros:
        vetor: Lista ordenada de elementos onde será realizada a busca.
        x: Valor a ser procurado na lista.
        inicio: Índice inicial do intervalo de busca.
        fim: Índice final do intervalo de busca.

    Returna:
        O índice inteiro correspondente à posição do elemento na lista ou -1 se o elemento não for encontrado.
    """
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] == x:
            return meio
        elif vetor[meio] < x:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

vetor = [3, 4, 5, 6, 7, 8, 9]
x = 4
resultado = pesquisa_binaria(vetor, x, 0, len(vetor) - 1)
if resultado != -1:
    print(f"Elemento encontrado no índice: {resultado}")
else:
    print("Elemento não encontrado no vetor.")