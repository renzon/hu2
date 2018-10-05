from functools import wraps
from time import strftime


#

# class log:
#     def __init__(self, *, fmt):
#         self.fmt = fmt
#
#     def __call__(self, f):
#         @wraps(f)
#         def f_logada(*args, **kwargs):
#             print(strftime(self.fmt))
#             return f(*args, **kwargs)
#
#         return f_logada


def log(g=None, *, fmt='%H:%M:%S'):
    if g is not None:
        return log(fmt=fmt)(g)

    def decorator(f):
        @wraps(f)
        def f_logada(*args, **kwargs):
            print(strftime(fmt))
            return f(*args, **kwargs)

        return f_logada

    return decorator


@log(fmt='%Y/%m/%d %H:%M:%S')
def ola(nome):
    """ Função que imprime o nome

    :param nome:
    :return:
    """
    print(f'Olá {nome}')


@log
def tratar_request():
    print('Tratando request')


# tratar_request = log(tratar_request)

tratar_request()
ola('Renzo')
print(ola.__name__)
print(help(ola))
