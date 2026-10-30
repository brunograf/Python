from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho / 1000000
        self._extensao = self.__class__.__name__.lower()
    
    @property
    def nome_completo(self):
        return f'{self.nome}.{self._extensao}({self.tamanho}MB)'

    @property
    def extensao(self):
        return self._extensao.lower()

    @extensao.setter
    def extensao(self):
        raise PermissionError('Você não pode alterar a extensão do arquivo')

    @abstractmethod
    def abrir(self):
        pass

class DOC(Arquivo):
    def abrir(self):
        return print(f'Abrindo o arquivo {self.nome_completo} no Microsoft Word!')

class PDF(Arquivo):
    def abrir(self):
        return print(f'Abrindo o arquivo {self.nome_completo} no Adobe Reader!')

def abrir(arquivo):
    arquivo.abrir()

def main():
    a1 = DOC('prova', 250000)
    a2 = PDF('relatório', 1300000)
    abrir(a1)
    abrir(a2)
    print(a2.nome_completo)

if __name__ == '__main__':
    main()