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
        try:
            return int(n)
        except ValueError:
            print('ERRO: Digite um número inteiro válido.')

def leiaFloat(msg):
    '''
    Lê um número real da entrada do usuário. Continua pedindo até que um valor válido seja digitado.

    Parâmetros:
        msg: Mensagem exibida para solicitar o número ao usuário.

    Retorna:
        O valor real informado pelo usuário.
    '''
    while True:
        n = input(msg)
        try:
            return float(n)
        except ValueError:
            print('ERRO: Digite um número real válido.')


nint = leiaInt('Digite um número: ')
nreal = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {nint} e o número real {nreal}.')