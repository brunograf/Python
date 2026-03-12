peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}. Você está com o peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}. Você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade.')
else:
    print(f'Seu IMC é {imc:.1f}. Você está com obesidade mórbida.')