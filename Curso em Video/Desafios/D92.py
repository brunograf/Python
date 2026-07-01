from datetime import date
CTPS = {}
CTPS['Nome'] = str(input('Nome: '))
CTPS['Idade'] = int(input('Idade: '))
CTPS['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if CTPS['CTPS'] != 0:
    CTPS['Ano de Contratação'] = int(input('Ano de Contratação: '))
    CTPS['Salário'] = float(input('Salário: '))
    CTPS['Aposentadoria'] = CTPS['Idade'] + ((CTPS['Ano de Contratação'] + 35) - date.today().year)
print('-=' * 30)
for k, v in CTPS.items():
    print(f'  - {k} tem o valor {v}')