total = 0
caro = 0
preco_barato = 1000
nome_barato = ''
while True:
    nome = str(input('Qual produto você adicionou no carrinho? '))
    preco = float(input('E qual é o preço do produto? '))
    total = total + preco
    if preco > 1000:
        caro = caro + 1
    if preco < preco_barato:
        preco_barato = preco
        nome_barato = nome
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    print ('-' * 30)
print (f'O total da compra foi R${total:.2f}.')
print (f'{caro} produtos custaram mais de R$1000.00.')
print (f'O produto mais barato foi {nome_barato}, que custou R${preco_barato:.2f}.')