def aumentar(dinheiro = 0, taxa = 0):
    res = dinheiro + (dinheiro * taxa / 100)
    return res

def diminuir(dinheiro = 0, taxa = 0):
    res = dinheiro - (dinheiro * taxa / 100)
    return res

def dobro(dinheiro = 0):
    res = dinheiro * 2
    return res

def metade(dinheiro = 0):
    res = dinheiro / 2
    return res

def moeda(dinheiro=0, moeda='R$'):
    res = f'{moeda}{dinheiro:.2f}'.replace('.', ',')
    return res