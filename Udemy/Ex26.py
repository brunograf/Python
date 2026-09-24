from dataclasses import dataclass

@dataclass(frozen=True)
class Ponto:
    """
    Representa um ponto no espaço 2D com coordenadas x e y.
    
    Parâmetros:
        x: Coordenada x do ponto (float)
        y: Coordenada y do ponto (float)
    """
    x: float
    y: float

p = Ponto(3, 4)
try:
    p.x = 5
except Exception as e:
    print(f"Erro: {e}")