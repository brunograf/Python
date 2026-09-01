class Usuario:
    def __init__(self, nome):
        self.nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
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