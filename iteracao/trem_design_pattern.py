"""
>>> trem = Trem(3)
>>> for vagao in trem:
...     print(vagao)
...
Vagao #1
Vagao #2
Vagao #3

"""


class TremIterable:
    def __init__(self, ultimo_vagao):
        self.ultimo_vagao = ultimo_vagao
        self.cursor=0

    def __next__(self):
        self.cursor+=1
        if self.cursor <=self.ultimo_vagao:
            return f'Vagao #{self.cursor}'
        raise StopIteration()


class Trem:
    def __init__(self, vagoes):
        self.vagoes = vagoes

    def __iter__(self):
        """ Retorna um iterável de vagoes

        :return:
        """
        return TremIterable(self.vagoes)
