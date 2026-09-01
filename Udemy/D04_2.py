import json
from D04_1 import Desenvolvedor


with open('dev.json', 'r') as arquivo:
    dev_data = json.load(arquivo)
    dev = Desenvolvedor(**dev_data)

print(f'Nome: {dev.nome}')
print(f'Sobrenome: {dev.sobrenome}')
print(f'Idade: {dev.idade}')
print(f'Altura: {dev.altura}')
print(f'Números Preferidos: {dev.numeros_preferidos}')
print(f'É Desenvolvedor: {dev.dev}')
print(f'Linguagens: {dev.linguagens}')