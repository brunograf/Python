def multiplicador (n):
    """
    Retorna uma função que multiplica o argumento por `n`.

    Parâmetros:
    n (int): O fator de multiplicação.

    Retorna:
    function: Uma função que multiplica o argumento por `n`.
    """
    def multiplicar (x):
        """
        Multiplica o argumento por `n`.

        Parâmetros:
        x (int): O número a ser multiplicado.

        Retorna:
        int: O resultado da multiplicação.
        """
        return x * n
    return multiplicar

dobrar = multiplicador(2)
triplicar = multiplicador(3)

print(dobrar(10))
print(triplicar(10))