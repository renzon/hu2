"""
Escreva uma funcao contagem de letras de acordo com o doctest:

>>> conta_letras('Renzo Nuccitelli')
{'r': 1, 'e': 2, 'n': 2, 'z': 1, 'o': 1, ' ': 1, 'u': 1, 'c': 2, 'i': 2, 't': 1, 'l': 2}

"""
from collections import defaultdict


def conta_letras(s):
    s = s.lower()
    dct = defaultdict(lambda: 0)
    for c in s:
        dct[c] += 1
    return dict(dct.items())
