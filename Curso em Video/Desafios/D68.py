from random import randint
c = 0
while True:
    print ('Vamos jogar par ou ímpar!')
    jogador_escolha = str(input('Par ou ímpar? [P/I] ')).upper()
    if jogador_escolha == 'P':
        computador_escolha = 'I'
    else:
        computador_escolha = 'P'
    jogador_numero = int(input('Digite um número (0 a 10): '))
    computador_numero = randint(0, 10) 
    soma = jogador_numero + computador_numero
    if soma % 2 == 0 and jogador_escolha == 'P':
        print (f'Parabéns, a soma deu {soma}, um número par, você ganhou!')
        c += 1
    elif soma % 2 == 1 and jogador_escolha == 'I':
        print (f'Parabéns, a soma deu {soma}, um número ímpar, você ganhou!')
        c += 1
    else:
        print (f'Que pena, a soma deu {soma}. Você perdeu!')
        break
print (f'Vocês ganhou {c} vezes antes de perder.')