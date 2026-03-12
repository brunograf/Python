from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print(f'Você tem {idade} anos, categoria MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos, categoria INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos, categoria JÚNIOR.')
elif idade <= 20:
    print(f'Você tem {idade} anos, categoria SÊNIOR.')
else:
    print(f'Você tem {idade} anos, categoria MASTER.')