class Autor:
    """
    Representa o autor de uma obra literária. Armazena o nome usado para identificar o autor.

    Parâmetros:
        nome: O nome do autor.
    """
    def __init__(self, nome):
        """
        Cria um autor com o nome informado. Mantém o nome disponível para identificação da autoria.

        Parâmetros:
            nome: O nome do autor.
        """
        self.nome = nome

class Livro:
    """
    Representa um livro com título e autor.

    Parâmetros:
        titulo: O título do livro.
        autor: O autor do livro.
    """
    def __init__(self, titulo, autor):
        """
        Cria um livro com o título e autor informados. Mantém essas informações disponíveis para consulta.
        
        Parâmetros:
            titulo: O título do livro.
            autor: O autor do livro.
        """
        self.titulo = titulo
        self.autor = autor

autor = Autor("J.K. Rowling")
livro = Livro("Harry Potter e a Pedra Filosofal", autor)

print(f"Livro: {livro.titulo}")
print(f"Autor: {livro.autor.nome}")