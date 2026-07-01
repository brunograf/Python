num = int(input("Digite um número inteiro: "))
base = int(input("Digite a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nResposta: "))
if base == 1:
    print(f"{num} convertido para binário é {bin(num)[2:]}")
elif base == 2:
    print(f"{num} convertido para octal é {oct(num)[2:]}")
elif base == 3:
    print(f"{num} convertido para hexadecimal é {hex(num)[2:]}")