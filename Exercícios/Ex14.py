n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print (f"Sua média foi {m:.1f}")
if m >= 7:
    print("E você foi aprovado! Parabéns!")
else:    
    print("E infelizmente você foi reprovado")