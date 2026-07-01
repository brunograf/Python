casa = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o salário do comprador? "))
anos = int(input("Em quantos anos ele pretende pagar? "))
prestacao = casa / (anos * 12)
minimo = salario * 0.3
if prestacao <= minimo:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo negado.")