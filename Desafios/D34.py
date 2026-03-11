salario_atual = float(input('Digite o salário atual do funcionário: R$'))
if salario_atual <= 1250:
    aumento = salario_atual * 0.15
    print(f'O salário do funcionário será aumentado em 15%, totalizando R${salario_atual + aumento:.2f}.')
else:
    aumento = salario_atual * 0.10
    print(f'O salário do funcionário será aumentado em 10%, totalizando R${salario_atual + aumento:.2f}.')