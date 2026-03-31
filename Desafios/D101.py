def voto(ano):
    '''
    Calcula se uma pessoa tem direito a voto ou não, com base na sua idade.

    Parâmetros:
    ano : O ano de nascimento da pessoa.

    Retorna:
        Uma string que indica se a pessoa tem direito a voto, e qual o tipo de voto.
    '''
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))