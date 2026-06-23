def func():
    print('Função iniciada')
    yield
    print('Função finalizada')

try:
    g = func()
    print(type(g))
    next(g)
    next(g)
except StopIteration as e:
    pass