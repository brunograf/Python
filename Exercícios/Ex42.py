try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: O denominador não pode ser zero.")
except TypeError:
    print("Erro: Tipo de dado inválido.")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
else:    
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre!")