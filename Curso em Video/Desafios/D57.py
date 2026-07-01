sexo = str(input('Digite o sexo do participante [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo inválido. Tente novamente.')
    sexo = str(input('Digite o sexo do participante [M/F]: ')).upper()
print('Registrado com sucesso!')