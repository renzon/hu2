from functools import wraps
from time import strftime


def log(f):
    @wraps(f)
    def f_logada(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*args, **kwargs)

    return f_logada


@log
def tratar_request():
    print('Tratando request')


@log
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
