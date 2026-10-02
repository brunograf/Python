from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        etiqueta = Panel(f"{self.nome:^20}\n{'':-^20}\n{f'R${self.preco:.2f}':.^20}", title="Produto", border_style="bold red", expand=False)
        return etiqueta

p1 = Produto("Camiseta", 49.90)
print(p1.etiqueta())
p2 = Produto("Calça Jeans", 89.90)
print(p2.etiqueta())