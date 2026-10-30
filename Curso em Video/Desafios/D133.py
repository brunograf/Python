from abc import ABC, abstractmethod
from rich import print

class Funcionário(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario
    
    def __str__(self):
        return f'{self.nome} ganha R${self.salario:.2f} e por ser {self.__class__.__name__} recebe um bônus de R${self.calcular_bonus():.2f}'
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > self.salario:
            self._salario = novo_salario
        else:
            raise ValueError('O novo salário não pode ser menor que o atual!')
    
    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionário):
    def calcular_bonus(self):
        return self.salario * 0.15

class Programador(Funcionário):
    def calcular_bonus(self):
        return self.salario * 0.10

class Designer(Funcionário):
    def calcular_bonus(self):
        return self.salario * 0.08

def main():
    gerente = Gerente('João', 5000)
    programador = Programador('Maria', 4000)
    designer = Designer('Pedro', 3000)

    print(gerente)
    print(programador)
    print(designer)
    
    designer.salario = 3500
    print(designer)
    programador.salario = 3899

if __name__ == '__main__':
    main()