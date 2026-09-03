class Animal:
    """
    Classe base para representar um animal.
    
    Parâmetros:
        nome: O nome do animal.
    """
    def __init__(self, nome):
        """
        Inicializa um animal com o nome fornecido.
    
        Parâmetros:
            nome: O nome do animal.
        """    
        self.nome = nome
    
    def respirar(self):
        """
        Método que simula a respiração do animal.
        """
        print(f"{self.nome} está respirando.")
    
    def fazer_som(self):
        """
        Método que simula o som que o animal faz.
        """
        print("...")

class Cachorro(Animal):
    """
    Classe derivada que representa um cachorro, herdando de Animal.
    
    Parâmetros:
        nome: O nome do cachorro.
    """
    def __init__(self, nome):
        """
        Inicializa um cachorro com o nome fornecido, chamando o construtor da classe base Animal.
        
        Parâmetros:
            nome: O nome do cachorro.
        """
        super().__init__(nome)
    
    def fazer_som(self):
        """
        Método que simula o latido que o cachorro faz.
        """
        print(f"{self.nome} diz: Au au!")

class Gato(Animal):
    """
    Classe derivada que representa um gato, herdando de Animal.
    
    Parâmetros:
        nome: O nome do gato.
    """
    def __init__(self, nome):
        """
        Inicializa um gato com o nome fornecido, chamando o construtor da classe base Animal.
        
        Parâmetros:
            nome: O nome do gato.
        """
        super().__init__(nome)
    
    def fazer_som(self):
        """
        Método que simula o miado que o gato faz.
        """
        print(f"{self.nome} diz: Miau!")

dog = Cachorro("Rex")
dog.respirar()
dog.fazer_som()

cat = Gato("Whiskers")
cat.respirar()
cat.fazer_som()