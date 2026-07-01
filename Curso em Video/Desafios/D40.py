nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f"Sua média é {media:.1f}. Infelizmente você foi reprovado.")
elif 5.0 <= media < 7.0:
    print(f"Sua média é {media:.1f}. Você está de recuperação.")
else:
    print(f"Sua média é {media:.1f}. Parabéns, você foi aprovado!")