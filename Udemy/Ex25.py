from dataclasses import dataclass

@dataclass
class Produto:
    """
    Representa um produto com nome, preço e quantidade em estoque.
    
    Parâmetros:
        nome: Nome do produto (str)
        preco: Preço do produto (float)
        estoque: Quantidade em estoque (int)
    """
    nome: str
    preco: float
    estoque: int = 0
    
    def disponivel(self):
        """
        Verifica se o produto está disponível em estoque.
        
        Retorna:
            bool: True se o produto estiver disponível, False caso contrário.
        """
        return self.estoque > 0
    
    def aplicar_desconto(self, percentual):
        """
        Aplica um desconto ao preço do produto.
        
        Parâmetros:
            percentual: Percentual de desconto (float)
        """
        self.preco -= self.preco * (percentual / 100)

p1 = Produto('Teclado', 250.0, 5)
p2 = Produto('Mouse', 150.0, 0)
print(p1.disponivel())
p1.aplicar_desconto(10)
print(p1.preco)
print(p1 == p2)