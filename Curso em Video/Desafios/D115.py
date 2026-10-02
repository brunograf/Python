from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/blue]! Sou {self.cargo} no setor {self.setor} da empresa Curso em Vídeo."

f1 = Funcionario("João", "Financeiro", "Analista")
print(f1.apresentar())
f2 = Funcionario("Maria", "Recursos Humanos", "Coordenadora")
print(f2.apresentar())