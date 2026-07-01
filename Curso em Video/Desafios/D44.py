preco = float(input('Digite o preço do produto: R$'))
pagamento = int(input('Digite a forma de pagamento:\n1 - À vista no dinheiro ou cheque\n2 - À vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão\nPagamento: '))
if pagamento == 1:
    preco = preco - (preco * 10 / 100)
elif pagamento == 2:
    preco = preco - (preco * 5 / 100)
elif pagamento == 3:
    preco = preco
elif pagamento == 4:
    preco = preco + (preco * 20 / 100)
print(f'Com o pagamento {pagamento}, o produto custa R${preco:.2f}')