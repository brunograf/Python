import json

dev = {
    'nome': 'Bruno',
    'sobrenome': 'Graf',
    'idade': 26,
    'altura': 1.82,
    'numeros_preferidos': (7, 20, 100),
    'dev': True,
    'linguagens': ['Python', 'HTML', 'CSS', 'JavaScript']
}

with open('dev.json', 'w') as arquivo:
    json.dump(dev, arquivo, indent=4)

with open('dev.json', 'r') as arquivo:
    dev = json.load(arquivo)
    for chave, valor in dev.items():
        print(f'{chave}: {valor}')
