def linha (tam = 42):
    return '-' * tam

def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        n = input(msg)
        try:
            return int(n)
        except ValueError:
            cabecalho(f'\033[31mERRO: Digite um número inteiro válido.\033[m')

def menu (lista):
    cabecalho('SISTEMA DE CADASTRO DE PESSOAS')
    for i, item in enumerate(lista):
        print(f'\033[33m{i+1}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc