from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []
    
    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos = sorted(self.jogos_favoritos)
    
    def ficha(self):
        ficha = Panel(f"Nome real: [black on blue] {self.nome} [/black on blue]\nJogos favoritos:\n{chr(10).join([f':video_game: [blue]{jogo}[/blue]' for jogo in self.jogos_favoritos])}", title= f"Jogador <{self.nick}>", expand=False)
        return print(ficha)

j1 = Gamer("Bruno Graf", "Brunelson")
j1.add_favoritos("God of War")
j1.add_favoritos("Dragon Age")
j1.add_favoritos("Graveyard Keeper")
j1.ficha()

j2 = Gamer("Juliane Moura", "Juju")
j2.add_favoritos("Asseto Corsa")
j2.add_favoritos("Forza Horizon 5")
j2.add_favoritos("Tekken 3")
j2.ficha()