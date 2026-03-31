def notas(*notas, sit=False):
    '''
    Analisa as notas fornecidas e retorna um dicionário com estatísticas.

    Parâmetros:
        *notas: Uma quantidade variável de notas (números).
        sit: Indica se a situação do aluno deve ser incluída na análise.

    Retorna:
        Um dicionário contendo:
            - total: O número total de notas.
            - maior: A maior nota.
            - menor: A menor nota.
            - média: A média das notas.
            - situação: A situação do aluno (opcional).
    '''
    resultado = {
        'total': len(notas),
        'maior': max(notas), 
        'menor': min(notas), 
        'média': sum(notas) / len(notas)
        }
    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'BOA'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'RAZOÁVEL'
        else:
            resultado['situação'] = 'RUIM'
    return resultado


resp = notas(5.5, 9.5, 10, 6.5, sit = True)
print(resp)