lista = [1, 2, 3, 4, 5]

for n in lista:
    print(n)

interador = iter(lista)
try:
    while True:
        print(next(interador))
except StopIteration as e:
    print("Fim da iteração")