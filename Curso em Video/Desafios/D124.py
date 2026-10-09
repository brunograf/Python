from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
    
    @abstractmethod
    def calcular_frete(self):
        pass
    
class Moto(Transporte):
    def __init__(self, distancia, fator = 0.5):
        super().__init__(distancia)
        self.fator = fator
    
    def calcular_frete(self):
        frete = self.fator * self.distancia
        return f"R${frete:.2f}"

class Caminhao(Transporte):
    def __init__(self, distancia, fator = 1.2):
        super().__init__(distancia)
        self.fator = fator

    def calcular_frete(self):
        if self.distancia < 50:
            return "Raio mínimo de 50Km"
        else:
            frete = self.fator * self.distancia
            return f"R${frete:.2f}"

class Drone(Transporte):
    def __init__(self, distancia, fator = 9.5):
        super().__init__(distancia)
        self.fator = fator
        
    def calcular_frete(self):
        if self.distancia > 10:
            return "Raio máximo de 10Km"
        else:
            frete = self.fator * self.distancia
            return f"R${frete:.2f}"

entrega = Moto(10)
print(f"Frete de {type(entrega).__name__} em {entrega.distancia}Km: {entrega.calcular_frete()}")
print()
entrega2 = Caminhao(30)
print(f"Frete de {type(entrega2).__name__} em {entrega2.distancia}Km: {entrega2.calcular_frete()}")
print()
entrega3 = Drone(5)
print(f"Frete de {type(entrega3).__name__} em {entrega3.distancia}Km: {entrega3.calcular_frete()}")


