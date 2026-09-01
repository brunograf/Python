class Cachorro:
    """
    Representa um cachorro com nome, raça e atributo de classe 'especie'.

    Atributos:
        especie: A espécie do cachorro. É um atributo de classe.
        nome: O nome do cachorro.
        raca: A raça do cachorro.
    """
    especie = "Canis lupus familiaris"
    def __init__(self, nome, raca):
        """
        Inicializa uma instância do objeto Cachorro com o nome e raça fornecidos.

        Parâmetros:
            nome: O nome do cachorro.
            raca: A raça do cachorro.
        """
        self.nome = nome
        self.raca = raca

    def latir(self):
        """
        Retorna uma string com o cachorro latindo.

        Retorna:
            str: A string com o cachorro latindo.
        """
        return f"{self.nome} diz: au au!"
    
    def apresentar(self):
        """
        Retorna uma string com a apresentação do cachorro.

        Retorna:
            str: A string com a apresentação do cachorro.
        """
        return f"Sou {self.nome}, um {self.raca}."
    
    def comendo(self, comida):
        """
        Retorna uma string indicando que o cachorro está comendo.

        Parâmetros:
            comida: A comida que o cachorro está comendo.

        Retorna:
            str: A string indicando que o cachorro está comendo.
        """
        return f"{self.nome} está comendo {comida}."

dog1 = Cachorro("Rex", "Labrador")
dog2 = Cachorro("Bella", "Poodle")

print(dog1.latir())
print(dog2.apresentar())
print(dog1.comendo("ração"))
print('-'*30)
print(dog1.nome)
print(dog2.raca)
print('-'*30)
print(Cachorro.especie)
print(dog1.especie)