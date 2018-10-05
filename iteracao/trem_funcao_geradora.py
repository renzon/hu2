"""
>>> trem = Trem(3)
>>> for vagao in trem:
...     print(vagao)
...
Vagao #1
Vagao #2
Vagao #3

"""


class Trem:
    def __init__(self, vagoes):
        self.vagoes = vagoes

    def __iter__(self):
        """ Retorna um iterável de vagoes

        :return:
        """
        vagoes = self.vagoes
        for vagao in range(1, vagoes+1):
            yield f'Vagao #{vagao}'
