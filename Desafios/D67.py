while True:
    n = int (input ('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    print (f'====== TABUADA DE {n} =======')
    for c in range (1, 11):
        print (f'{n} x {c} = {n*c}')
    print ('====== FIM ======')
print ('Você digitou um valor negativo. Encerrando...')