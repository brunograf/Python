with open ('dados.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

with open ('dados.txt', 'r') as arquivo:
    print(arquivo.read())