num = 0
c = 0
s = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    s += num
    c += 1
print(f'Foram digitados {c} valores e a soma deles é {s}')