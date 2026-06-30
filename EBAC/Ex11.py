def ordenacao_bolha(vetor):
    """
    Ordena uma lista de valores utilizando o algoritmo de ordenação por bolha.

    Parâmetros:
        vetor: Lista de valores comparáveis que será ordenada.

    Retorna:
        Uma lista contendo os mesmos elementos de entrada organizados em ordem crescente.
    """
    for i in range(len(vetor) - 1, 0, -1):
        for j in range(0, i):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor

vetor = [64, 34, 25, 12, 22, 11, 90]
print(f"Vetor original: {vetor}")
vetor_ordenado = ordenacao_bolha(vetor)
print(f"Vetor ordenado: {vetor_ordenado}")