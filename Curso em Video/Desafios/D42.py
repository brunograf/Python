r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é ESCALENO.')
    else:
        print('O triângulo é ISÓSCELES.')
else:
    print('As retas não podem formar um triângulo.')