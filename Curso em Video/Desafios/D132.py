from rich import print
from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento
        
    @property
    def nascimento(self):
        return self._nascimento
    
    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError("Ano {ano} é inválido")
    
    @property
    def idade(self):
        return date.today().year - self._nascimento
    
    @idade.setter
    def idade(self, valor):
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")
        
class Aluno(Pessoa):
    cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais")
    
    def add_curso(self, curso):
        curso = curso.strip().upper()
        if 3 <= len(curso) <= 5:
            self.cursos_oficiais.append(curso)
        else:
            raise ValueError("O nome do curso {curso} está fora do padrão")

    def __str__(self):
        return f'Nome: {self._nome} | Nascimento: {self._nascimento} | Curso: {self._curso}'

if __name__ == "__main__":
    aluno = Aluno("João", 2000, "ADS")
    print(aluno)
    aluno.add_curso("HIST")
    print(aluno.cursos_oficiais)