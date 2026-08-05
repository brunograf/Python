def soma (*args):
    """
    Soma os valores passados como argumentos e retorna o resultado.

    Parâmetros:
    *args (int or float): Valores a serem somados.

    Retorna:
    int or float: A soma dos valores.
    """
    return sum(args)

print(soma(1, 2, 3, 4, 5))