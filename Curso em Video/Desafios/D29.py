vel = float(input('Qual a velocidade que o carro está? '))
if vel > 80:
    print('Multe o motorista por excesso de velocidade!')
    multa = (vel - 80) * 7
    print(f'O valor da multa é R${multa:.2f}.')
else:
    print('Tudo certo. Ele está dentro do limite de velocidade.')