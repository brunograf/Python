def fatorial(n, show=False):
    '''
    Calcula o fatorial de um número inteiro não negativo. Pode opcionalmente exibir o cálculo.

    Parâmetros:
        n: Número inteiro não negativo cujo fatorial será calculado.
        show: Indica se o cálculo detalhado deve ser exibido.

    Retorna:
        O valor inteiro correspondente ao fatorial de n.
    '''
    if n == 0 or n == 1:
        return 1
    else:
        resultado = n * fatorial(n - 1)
        if show:
            for i in range(n, 0, -1):
                print(i, end=' ')
                if i > 1:
                    print('x', end=' ')
                else:                    
                    print('=', end=' ')
            print(resultado)
        return resultado


num = int(input("Digite um número para calcular o fatorial: "))
show_calculo = input("Deseja mostrar os passos? (s/n): ").lower() == 's'
print(f"O fatorial de {num} é {fatorial(num, show_calculo)}")