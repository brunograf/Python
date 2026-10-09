from abc import ABC, abstractmethod
from rich import print
from random import randint

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
    
    def atacar(self, alvo, forca):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[randint(0, len(self.golpes) - 1)]
            print(f"[blue]{self.nome}[/] atacou [green]{alvo.nome}[/] com [red]{golpe}[/]")
            alvo.receber_dano(forca)
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")
    def receber_dano(self, forca):
        dano = randint(0, forca)
        self.vida -=   dano
        if self.vida < 0:
            self.vida = 0
        print(f"[blue]{self.nome}[/] recebeu [red]{dano} de dano[/]!")

    @abstractmethod
    def curar(self):
        cura = randint(0, 100)
        self.vida = self.vida + cura
        if self.vida > 100:
            self.vida = 100
        else:
            print(f"[blue]{self.nome}[/] curou [green]{cura} de vida[/] com [yellow]magia de cura[/]!")

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Corte de Espada", "Voadora", "Martelada"]

    def curar(self):
        cura = randint(0, 100)
        self.vida += cura
        if self.vida > 100:
            self.vida = 100
        else:
            print(f"[blue]{self.nome}[/] [magenta]usou uma atadura[/] e curou [green]{cura} de vida[/]!")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Relâmpago", "Raio de Gelo", "Misseis Mágicos"]

    def curar(self):
        cura = randint(0, 100)
        self.vida += cura
        if self.vida > 100:
            self.vida = 100
        else:
            print(f"[blue]{self.nome}[/] curou [green]{cura} de vida[/] com [yellow]magia de cura[/]!") 

p1 = Guerreiro("Jorge", 100)
p2 = Mago("Osmar", 80)

p1.atacar(p2, 30)
p2.curar()
p2.atacar(p1, 20)