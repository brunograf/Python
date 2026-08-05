a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f'Uniao: {a | b} \nInterseccao: {a & b} \nDiferenca: {a - b} \nDiferenca Simetrica: {a ^ b}') 

a.add(5)
b.discard(6)

print(a)
print(b)