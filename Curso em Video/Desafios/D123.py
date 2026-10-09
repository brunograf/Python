from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self, nome):
        self.nome = nome

    def preparar(self):
        print(f"--- Iniciando o preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f"--- Bebida pronta ---")
    
    def ferver_agua(self):
        print("1. Fervendo água a 100°C")
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__("Café")
    
    def misturar(self):
        print("2. Coando o café moído na água fervente")

    def servir(self):
        print("3. Servindo em xícara pequena")

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__("Chá")
    
    def misturar(self):
        print("2. Colocando o sachê de chá na água fervente")

    def servir(self):
        print("3. Servindo em xícara de porcelana com limão")

class Leite(BebidaQuente):
    def __init__(self):
        super().__init__("Leite")
    
    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite")

    def servir(self):
        print("3. Servindo na xícara grande, já com café")

bebida = Cafe()
bebida.preparar()
print()
bebida2 = Cha()
bebida2.preparar()