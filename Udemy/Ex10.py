from itertools import combinations, permutations, product

pessoas = ['Bruno', 'Juju', 'Alice']

camisetas = [
    ['preta', 'branca', 'vermelha'],
    ['p', 'm', 'g'],
    ['algodão', 'linho']
]

print('COMBINAÇÕES:')
print(*list(combinations(pessoas, 2)), sep='\n')

print('PERMUTAÇÕES:')
print(*list(permutations(pessoas, 2)), sep='\n')

print('PRODUTO:')
print(*list(product(*camisetas)), sep='\n')