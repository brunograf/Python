from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto, salario, sal_min = 1612, inss = 7.5):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss
    
    @abstractmethod
    def calcular_sal(self):
        pass

    def analisar_sal(self):
        ficha = Panel(f"O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario / self.sal_min:.1f} salários mínimos[/].", title="Análise de salário", width=45)
        return print(ficha)
        
class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab = 220):
        super().__init__(nome, valor_hora, horas_trab)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calcular_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        return self.salario

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto, 0)
        
    def calcular_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        return self.salario

f1 = Horista("Paulo", 12, 200)
f1.calcular_sal()
f1.analisar_sal()

f2 = Mensalista("Amanda", 9500)
f2.calcular_sal()
f2.analisar_sal()