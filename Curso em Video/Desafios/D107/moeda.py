def aumentar(dinheiro, taxa):
    res = dinheiro + (dinheiro * taxa / 100)
    return res

def diminuir(dinheiro, taxa):
    res = dinheiro - (dinheiro * taxa / 100)
    return res

def dobro(dinheiro):
    res = dinheiro * 2
    return res

def metade(dinheiro):
    res = dinheiro / 2
    return res