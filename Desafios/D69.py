maior_idade = 0
homem = 0
mulher_jovem = 0
while True:
    idade = int(input('Quantos anos você tem? '))
    if idade >= 18:
        maior_idade = maior_idade + 1
    sexo = str(input('Qual é o seu sexo? [M/F] ')).upper()
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F' and idade < 20:
        mulher_jovem = mulher_jovem + 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    print ('-' * 30)
    if continuar == 'N':
        break
print (f'{maior_idade} pessoas tem mais de 18 anos.')
print (f'{homem} homens foram cadastrados.')
print (f'{mulher_jovem} mulheres tem menos de 20 anos.')