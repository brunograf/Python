class Usuario:
    """
    Representa um usuário identificado por um nome válido. Mantém o nome disponível para consulta e atualização.

    Parâmetros:
        nome: O nome do usuário.

    Levanta:
        ValueError: Se o nome não for um texto ou tiver menos de três caracteres.
    """
    def __init__(self, nome):
        """
        Cria um usuário com o nome informado. O nome é validado antes de ser armazenado.

        Parâmetros:
            nome: O nome do usuário.

        Levanta:
            ValueError: Se o nome não for um texto ou tiver menos de três caracteres.
        """
        self.nome = nome
    
    @property
    def nome(self):
        """
        Retorna o nome do usuário. O valor armazenado representa o nome atualmente associado ao usuário.

        Retorna:
            O nome do usuário.
        """
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        """
        Atualiza o nome do usuário após validar seu conteúdo. O nome deve ser um texto com pelo menos três caracteres.

        Parâmetros:
            valor: O novo nome do usuário.

        Retorna:
            None.

        Levanta:
            ValueError: Se o valor não for um texto ou tiver menos de três caracteres.
        """
        if not isinstance(valor, str):
            raise ValueError('Nome deve ser um texto.')
        if len(valor) < 3:
            raise ValueError('Nome deve ter pelo menos 3 caracteres.')
        self._nome = valor

u = Usuario('Bruno')
print(u.nome)
u.nome = 'Juju'
print(u.nome)

try:
    u.nome = 'Al'
except ValueError as e:
    print(e)
    
try:
    u.nome = 123
except ValueError as e:
    print(e)