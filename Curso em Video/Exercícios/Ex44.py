from rich import print

class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota
    
    @property
    def nota(self): #getter
        return self._nota

    @nota.setter
    def nota(self, nota): #setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("Nota inválida!")

av1 = Avaliacao("Pedro", "Matemática", 9.5)
av1.nota = 11
print(f"Nome: {av1.nome}\nDisciplina: {av1.disciplina}\nNota: {av1.nota}")