palin = str(input('Digite uma frase: ')).strip().lower()
palin = palin.replace(' ', '')
print(f'Essa palavra é palíndroma? {palin == palin[::-1]}')