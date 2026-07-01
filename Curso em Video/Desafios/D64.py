num = 0
c = 0
s = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        s += num
        c += 1
print(f'Foram digitados {c} números e a soma deles é {s}')