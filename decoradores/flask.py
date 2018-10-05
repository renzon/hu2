"""
>>> @rota('/')
... def raiz():
...     return 'home'
...
>>> raiz()
'home'
>>> executar('/')
'home'
>>> executar('/desconhecido')
404

"""

_rotas_dct = {}


def rota(caminho):
    def decorador(f):
        _rotas_dct[caminho] = f
        return f

    return decorador


# def raiz():
#    return 'home'
# raiz=rota('/')(raiz)

def executar(caminho):
    if caminho not in _rotas_dct:
        return 404
    f = _rotas_dct[caminho]
    return f()
