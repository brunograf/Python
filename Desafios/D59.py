n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('''===============================
    O que você quer fazer com os números?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
print ('Encerrando o programa...')