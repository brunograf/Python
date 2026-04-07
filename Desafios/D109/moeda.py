def aumentar(dinheiro = 0, taxa = 0, format = False):
    res = dinheiro + (dinheiro * taxa / 100)
    if format:
        res = moeda(res)
    return res

def diminuir(dinheiro = 0, taxa = 0, format = False):
    res = dinheiro - (dinheiro * taxa / 100)
    if format:
        res = moeda(res)
    return res

def dobro(dinheiro = 0, format = False):
    res = dinheiro * 2
    if format:
        res = moeda(res)
    return res

def metade(dinheiro = 0, format = False):
    res = dinheiro / 2
    if format:
        res = moeda(res)
    return res

def moeda(dinheiro=0, moeda='R$'):
    res = f'{moeda}{dinheiro:.2f}'.replace('.', ',')
    return res

def resumo(dinheiro=0, taxa_aum=0, taxa_dim=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(dinheiro)}')
    print(f'Dobro do preço: \t{dobro(dinheiro, True)}')
    print(f'Metade do preço: \t{metade(dinheiro, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(dinheiro, taxa_aum, True)}')
    print(f'{taxa_dim}% de redução: \t{diminuir(dinheiro, taxa_dim, True)}')