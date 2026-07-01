cadastro = {}
dados = []
mulheres = []
velhos = []
soma_idade = media_idade = 0
while True:
    cadastro['nome'] = input('Qual é o seu nome? ')
    cadastro['idade'] = int(input('Qual é a sua idade? '))
    soma_idade += cadastro['idade']
    cadastro['sexo'] = input('Qual é o seu sexo? [M/F] ').upper()
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro['nome'])
    dados.append(cadastro.copy())
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break
print(f'-=' * 30)
print(f'Foram cadastradas {len(dados)} pessoas.')
media_idade = soma_idade / len(dados)
print(f'A idade média das pessoas cadastradas é de {media_idade:.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}.')
for p in dados:
    if p['idade'] >= media_idade:
        velhos.append(p['nome'])
print(f'As pessoas mais velhas cadastradas foram: {velhos}.')