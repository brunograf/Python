def leiaInt(msg):
    '''
    Lê um número inteiro da entrada do usuário. Continua pedindo até que um valor válido seja digitado.

    Parâmetros:
        msg: Mensagem exibida para solicitar o número ao usuário.

    Retorna:
        O valor inteiro informado pelo usuário.
    '''
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('ERRO: Digite um número inteiro válido.')


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')