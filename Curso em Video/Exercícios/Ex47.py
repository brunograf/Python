class Carteira:
    def __init__(self, valor):
        self.__saldo = valor
    
    def __str__(self):
        return f"R${self.__saldo:.2f}"
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self):
        raise PermissionError("Você não tem permissão para mudar o saldo dessa forma")
    
    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False
    
    def __iadd__(self, valor):
        self.__saldo = self.__saldo + valor
        return self

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)
    print(c1)
    print(c1 == c2)
    c1 += 50
    print(c1)
    print(c1 == c2)

if __name__ == '__main__':
    main()