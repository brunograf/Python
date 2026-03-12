nome = str(input('Qual é o seu nome? '))
if nome == 'Bruno':
    print('Que nome bonito você tem!')
elif nome == 'Juju':
    print('Você tem um nome lindo, princesa!')
elif nome in 'Willy, Alice, Leopolda, Maíra, Lucas':
    print('Olá, membro da família Black Sheep!')
else:
    print('Seu nome é normal.')
print(f'Tenha um bom dia, {nome}!')