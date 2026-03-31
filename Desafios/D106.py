def pyHelp(comando):
    '''
    Imprime o manual do comando fornecido.

    Parâmetros:
        comando: O comando cujo manual deve ser impresso.
    '''
    print(f'\033[36m~\033[m' * 60 )
    print(f'\033[36mAcessando o manual do comando "{comando}"\033[m'.center(60))
    print(f'\033[36m~\033[m' * 60 )
    help(comando)


while True:
    print(f'\033[32m~\033[m' * 60 )
    print(f'\033[32mSISTEMA DE AJUDA PyHELP\033[m'.center(60))
    print(f'\033[32m~\033[m' * 60 )
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        print(f'\033[33m~\033[m' * 60 )
        print('\033[33mAté logo!\033[m')
        print(f'\033[33m~\033[m' * 60 )
        break
    else:
        pyHelp(comando)