soma_idade = 0
velho_idade = 0
homens = 0
mulheres = 0
for c in range (0, 4):
    nome = str(input('Digite o nome do participante: '))
    idade = int(input('Digite a idade do participante: '))
    soma_idade += idade
    sexo = str(input('Digite o sexo do participante [M/F]: ')).upper()
    if sexo == 'M' and idade > velho_idade:
        velho_idade = idade
        velho_nome = nome
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('=============================')
m = soma_idade / 4
print(f'A idade média dos participantes é de {m:.1f} anos.')
print(f'O nome do homem mais velho é {velho_nome}.')
print(f'E foram cadastradas {mulheres} mulheres com menos de 20 anos.')