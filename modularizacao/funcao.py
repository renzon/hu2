def f(name, middle='Santos', lastname='Nuccitelli'):
    return f'Olá {name} {middle} {lastname}'


a = None
print(a is None)
print(id(a) == id(None))
print(isinstance(a, str))
print(f('Renzo'))
print(f('Renzo', 'dos Santos'))
print(f('Renzo', lastname='Nucci'))
print(f('Renzo', lastname='Nucci'))
print(f('Renzo', lastname='Nucci', middle='Midle'))
print(f(lastname='Nucci', middle='Midle', name='Renzo'))
name = 'Luciano Ramalho Python'.split()
print(f(*name))


def soma(*args, **kwargs):
    return args, kwargs


print(soma())
print(soma(0))
print(soma(0, 3))
print(soma(0, 3, 5, name='Renzo', foo='bar'))
