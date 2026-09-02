class Usuario:
    """
    Representa um usuário com nome e endereço de email. Armazena informações de contato fornecidas na criação do objeto.

    Parâmetros:
        nome: O nome do usuário.
        email: O endereço de email do usuário.
    """
    def __init__(self, nome, email):
        """
        Cria um usuário com o nome e o email informados. Armazena os dados para consulta posterior.

        Parâmetros:
            nome: O nome do usuário.
            email: O endereço de email do usuário.
        """
        self.nome = nome
        self.email = email
    
    @classmethod
    def de_string(cls, string):
        """
        Cria um usuário a partir de uma string com nome e email separados por vírgula. Retorna um usuário com os valores extraídos.

        Parâmetros:
            string: Uma string contendo o nome e o email separados por vírgula.

        Retorna:
            Um usuário criado com os dados da string.
        """
        nome, email = string.split(',')
        return cls(nome, email)
    
    @classmethod
    def de_dicionario(cls, dicionario):
        """
        Cria um usuário a partir de um dicionário com dados de contato. Retorna um usuário preenchido com os valores do dicionário.

        Parâmetros:
            dicionario: Um dicionário contendo as chaves `nome` e `email`.

        Retorna:
            Um usuário criado com os dados do dicionário.
        """
        return cls(dicionario['nome'], dicionario['email'])


u1 = Usuario('Bruno', 'bruno@email.com')
u2 = Usuario.de_string('Juju,juju@email.com')
u3 = Usuario.de_dicionario({'nome': 'Alice', 'email': 'alice@email.com'})

print(u1.nome, u1.email)
print(u2.nome, u2.email)
print(u3.nome, u3.email)