class Jogador:
    """
    Representa um jogador identificado por um nome. Mantém a identificação do jogador para uso em um time.

    Parâmetros:
        nome: O nome do jogador.
    """
    def __init__(self, nome):
        """
        Cria um jogador com o nome informado. Armazena o nome para identificação posterior.

        Parâmetros:
            nome: O nome do jogador.
        """
        self.nome = nome

class Time:
    """
    Representa um time identificado por um nome. Mantém a lista de jogadores que compõem o time.

    Parâmetros:
        nome: O nome do time.
    """
    def __init__(self, nome):
        """
        Cria um time com o nome informado. Inicializa o time sem jogadores associados.

        Parâmetros:
            nome: O nome do time.
        """
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        """
        Adiciona um jogador à lista de jogadores do time.
        
        Parâmetros:
            jogador: O jogador a ser adicionado ao time.
        """
        self.jogadores.append(jogador)

j1 = Jogador("Bruno")
j2 = Jogador("Juju")

time = Time("Pythonistas")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)

print(f"Time: {time.nome}")
print("Jogadores:")
for jogador in time.jogadores:
    print(f"- {jogador.nome}")