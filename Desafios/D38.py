n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior que o segundo ({n2}).')
elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior que o primeiro ({n1}).')
else:
    print(f'Os dois valores são iguais ({n1}).')