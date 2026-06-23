def func():
    print('Função parte 1')
    
    x = yield
    print(x)
    print('Função parte 2')
    
    a = yield
    print(a)
    print('Função parte 3')

try:
    y = func()
    
    next(y)
    
    y.send(6)
    
    y.send(12)

except StopIteration as e:
    pass