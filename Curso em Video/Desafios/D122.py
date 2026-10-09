from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtde_lados):
        self.qtde_lados = qtde_lados

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.qtde_lados * self.lado

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)  # Círculo não tem lados
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio

quadrado = Quadrado(5)
print(f"Área do quadrado: {quadrado.area()}")
print(f"Perímetro do quadrado: {quadrado.perimetro()}")
print()
circulo = Circulo(3)
print(f"Área do círculo: {circulo.area()}")
print(f"Perímetro do círculo: {circulo.perimetro()}")