from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    def fvalor(self):
        return f'R${self._valor:.2f}'
    
    @abstractmethod
    def pagar(self):
        pass

class PIX(Pagamento):
    def pagar(self):
        return print(f'Pagamento confirmado de {self.fvalor} realizado com PIX')

class Credito(Pagamento):
    def pagar(self):
        return print(f'Pagamento confirmado de {self.fvalor} realizado com Crédito')

class Boleto(Pagamento):
    def pagar(self):
        return print(f'Pagamento confirmado de {self.fvalor} realizado com Boleto')

def finalizar_compra(pagamento):
    pagamento.pagar()

def main():
    finalizar_compra(PIX(100))
    finalizar_compra(Credito(200))
    finalizar_compra(Boleto(300))

if __name__ == '__main__':
    main()