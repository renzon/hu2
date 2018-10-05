from functools import wraps
from time import strftime


def log(*, fmt):
    def decorator(f):
        @wraps(f)
        def f_logada(*args, **kwargs):
            print(strftime(fmt))
            return f(*args, **kwargs)

        return f_logada

    return decorator


@log(fmt='%H:%M:%S')
def tratar_request():
    print('Tratando request')


@log(fmt='%Y/%m/%d %H:%M:%S')
def ola(nome):
    """ Função que imprime o nome

    :param nome:
    :return:
    """
    print(f'Olá {nome}')


# tratar_request = log(tratar_request)

tratar_request()
ola('Renzo')
print(ola.__name__)
print(help(ola))
