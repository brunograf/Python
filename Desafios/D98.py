from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        cont = i
        print(f'Contagem de {i} para {f} de {p} em {p}')
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont += p
        print('FIM')
    else:
        cont = i
        print(f'Contagem de {i} para {f} de {p} em {p}')
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.2)
            cont -= p
        print('FIM')


contador(1, 10, 1)
print('-=' * 20)
contador(10, 0, 2)
print('-=' * 20)
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))