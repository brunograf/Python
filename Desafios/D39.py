from datetime import date
ano = int(input("Informe o ano que você nasceu: "))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print(f"Você tem {idade} anos. Ainda faltam {18 - idade} anos para você se alistar.")
elif idade == 18:
    print(f"Você tem {idade} anos. Está na hora de se alistar!")
else:
    print(f"Você tem {idade} anos. Já passou {idade - 18} anos do prazo de alistamento.")