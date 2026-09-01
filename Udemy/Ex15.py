class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    @classmethod
    def de_string(cls, string):
        nome, email = string.split(',')
        return cls(nome, email)
    
    @classmethod
    def de_dicionario(cls, dicionario):
        return cls(dicionario['nome'], dicionario['email'])


u1 = Usuario('Bruno', 'bruno@email.com')
u2 = Usuario.de_string('Juju,juju@email.com')
u3 = Usuario.de_dicionario({'nome': 'Alice', 'email': 'alice@email.com'})

print(u1.nome, u1.email)
print(u2.nome, u2.email)
print(u3.nome, u3.email)