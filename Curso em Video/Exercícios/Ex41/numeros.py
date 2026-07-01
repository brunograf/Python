from Exercícios.Módulos.uteis.contas import contas

num = int(input("Digite um número inteiro: "))
fat = contas.fatorial(num)
print(f"O fatorial de {num} é: {fat}")
print(f"O dobro de {num} é: {contas.dobro(num)}")
print(f"O triplo de {num} é: {contas.triplo(num)}")