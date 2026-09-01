import json

class Desenvolvedor:
    def __init__(self, nome, sobrenome, idade, altura, numeros_preferidos, dev, linguagens):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.numeros_preferidos = numeros_preferidos
        self.dev = dev
        self.linguagens = linguagens

    def to_dict(self):
        return {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'idade': self.idade,
            'altura': self.altura,
            'numeros_preferidos': self.numeros_preferidos,
            'dev': self.dev,
            'linguagens': self.linguagens
        }

dev = Desenvolvedor(
    nome='Bruno',
    sobrenome='Graf',
    idade=26,
    altura=1.82,
    numeros_preferidos=(7, 20, 100),
    dev=True,
    linguagens=['Python', 'HTML', 'CSS', 'JavaScript']
)

with open('dev.json', 'w') as arquivo:
    json.dump(dev.to_dict(), arquivo, indent=4)