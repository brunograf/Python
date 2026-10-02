from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas
    
    def calcular_carne(self):
        carne_por_pessoa = 0.4  # kg por pessoa
        total_carne = self.pessoas * carne_por_pessoa
        return total_carne
    
    def custo_total(self):
        preco_carne = 82.5  # preço por kg
        total_carne = self.calcular_carne()
        custo_total = total_carne * preco_carne
        return custo_total
    
    def custo_por_pessoa(self):
        return self.custo_total() / self.pessoas
    
    def apresentar(self):
        apresentação = Panel(f"Analisando [green]{self.titulo}[/green] com [blue]{self.pessoas} convidados[/blue]\nCada partcipante comerá 0.4kg e cada quilo custa R$82.50\nRecomendo [yellow]comprar {self.calcular_carne():.2f}kg[/yellow] de carne\nO custo total será de [red]R${self.custo_total():.2f}[/red]\nCada pessoa pagará [magenta]R${self.custo_por_pessoa():.2f}[/magenta] para participar.", title=self.titulo, expand=False)
        return apresentação

churras = Churrasco("Churras do Bruninho", 10)
print(churras.apresentar())