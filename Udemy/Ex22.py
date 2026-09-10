class JsonMixin:
    """
    Fornece métodos para converter objetos em JSON e recriá-los a partir de JSON.
    """
    def to_json(self):
        """
        Converte os atributos do objeto em uma string JSON formatada. O resultado representa o estado atual do objeto.

        Retorna:
            str: Uma representação JSON formatada dos atributos do objeto.
        """
        import json
        return json.dumps(self.__dict__, indent=4)

    @classmethod
    def from_json(cls, texto):
        """
        Cria uma instância do objeto a partir de uma string JSON.

        Parâmetros:
            texto (str): Uma string JSON contendo os dados do objeto.

        Retorna:
            obj: Uma instância do objeto inicializada com os dados do JSON.
        """
        import json
        dados = json.loads(texto)
        obj = cls.__new__(cls)
        obj.__dict__.update(dados)
        return obj

class LogMixin:
        """
        Fornece um método para exibir mensagens associadas a um objeto. Cada mensagem identifica a classe responsável por ela.
        """
    def log(self, msg):
        """
        Exibe uma mensagem identificada pelo nome da classe do objeto. Isso ajuda a indicar a origem da mensagem.

        Parâmetros:
            msg (str): A mensagem que será exibida.
        """
        print(f'[{self.__class__.__name__}] {msg}')

class ValidacaoMixin:
    """
    Fornece validação para os atributos de um objeto. Garante que nenhum atributo tenha o valor None.
    """
    def validar(self):
        """
        Verifica se todos os atributos do objeto possuem valores válidos.

        Parâmetros:
            bool: True quando todos os atributos possuem valores válidos.

        Levanta:
            ValueError: Se algum atributo do objeto tiver o valor None.
        
        Retorna:
            bool: True se todos os atributos forem válidos.
        """
        for nome, valor in self.__dict__.items():
            if valor is None:
                raise ValueError(f'O atributo {nome} não pode ser None.')
        return True

class Usuario(JsonMixin, LogMixin, ValidacaoMixin):
    """
    Representa um usuário com nome e endereço de e-mail. Valida os dados e registra uma mensagem quando o usuário é criado.
    """

    def __init__(self, nome, email):
        """
        Inicializa um usuário com nome e endereço de e-mail. Os atributos fornecidos são validados durante a inicialização.

        Parâmetros:
            nome (str): O nome do usuário.
            email (str): O endereço de e-mail do usuário.

        Levanta:
            ValueError: Se o nome ou o e-mail tiver o valor None.
        """
        self.nome = nome
        self.email = email
        self.validar()
        self.log('Usuário criado com sucesso.')

u = Usuario('Bruno', 'bruno@email.com')
print(u.to_json())