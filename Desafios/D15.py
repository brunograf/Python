km = float (input("Quantos km você percorreu com o carro? "))
dias = int (input("Quantos dias você ficou com o carro? "))
preco = (km * 0.15) + (dias * 60)
print(f"O preço a pagar é: R$ {preco:.2f}")