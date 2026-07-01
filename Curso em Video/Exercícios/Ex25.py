num = [2, 5, 9, 1]
num [2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
if 4 in num:
    num.remove(2)
else:
    print('O valor 4 não foi encontrado na lista.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')