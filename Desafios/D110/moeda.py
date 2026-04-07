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