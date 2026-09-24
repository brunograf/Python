from dataclasses import dataclass

@dataclass(order=True)
class Produto:
    """
    Representa um produto com nome e preço.
    
    Parâmetros:
        nome: Nome do produto (str)
        preco: Preço do produto (float)
    """
    nome: str
    preco: float

produtos = [
    Produto('Teclado', 250.0),
    Produto('Mouse', 150.0),
    Produto('Monitor', 800.0),
    Produto('Cabo HDMI', 50.0)
]

produtos.sort()
for produto in produtos:
    print(f"{produto.nome}: R${produto.preco:.2f}")