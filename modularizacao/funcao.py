'Esse módulo demonstra uso de função e parâmetros'


def f(name: str, middle: str = 'Santos', lastname: str = 'Nuccitelli'):
    """Funcão f que mostra os parâmetros

    :param name: Nome
    :param middle: Meio
    :param lastname: Ultimo
    :return: string

    Ex:

    >>> f('Renzo', 'Santos', 'Nuccitelli')
    'Olá Renzo Santos Nuccitelli'

    """
    return f'Olá {name} {middle} {lastname}'


def soma(a, *args, last=9, **parcelas):
    return a, last, args, parcelas

if __name__ == '__main__':
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

    print(soma(8))
    print(soma(0))
    print(soma(0, 3))
    print(soma(0, 3, 5, name='Renzo', foo='bar'))

    person = {
        'name': 'Henzo',
        'age': 36,
        'last': 6,
    }
    print(soma(0, *person, **person))
