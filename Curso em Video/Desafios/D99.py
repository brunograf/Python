def maior(*num):
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='-> ')
    print()
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')
    print('-=' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)