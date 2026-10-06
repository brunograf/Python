from rich import print

class Caneta:
    def __init__(self, cor = "Azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True
    
    def escrever(self, msg):
        if self.tampada:
            print(f":warning: A caneta está tampada. Não é possível escrever.")
        else:
            print(f"{self.cor}{msg}[/]")
    
    def tampar(self):
        if self.tampada:
            print(f":warning: A caneta já está tampada.")
        else:
            self.tampada = True
            print(f":lock: A caneta foi tampada.")
    
    def destampar(self):
        if not self.tampada:
            print(f":warning: A caneta já está destampada.")
        else:
            self.tampada = False
            print(f":unlock: A caneta foi destampada.")
    
    def pular_linha(self, qtd=1):
        if self.tampada:
            print(f":warning: A caneta está tampada. Não é possível pular linhas.")
        else:
            print("\n" * qtd, end="")

c1 = Caneta("Azul")
c1.escrever("Olá, mundo!")
c1.destampar()
c1.escrever("Olá, mundo!")

c2 = Caneta("Vermelha")
c2.destampar()
c2.escrever("Olá, mundo!")
c2.escrever("Essa é uma caneta vermelha.")
c2.pular_linha(2)
c2.escrever("Essa é uma caneta vermelha com duas linhas puladas acima.")
c2.tampar()