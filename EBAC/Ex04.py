def func():
    x = 5
    print('Função parte 1')
    
    yield x
    x += 7
    print('Função parte 2')
    
    yield x
    
    print('Função parte 3')

try:
    y = func()
    
    z = next(y)
    print(z)
    
    z = next(y)
    print(z)
    
    z = next(y)
    print(z)
except StopIteration as e:
    pass