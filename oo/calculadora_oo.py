"""
>>> calculadora = Calculadora()
>>> calculadora.calcular('+', 3, 2)
5.0
>>> calculadora.adicionar_operacao('-', subtracao)
>>> calculadora.calcular('-', 3, 2)
1.0
"""


# Framework

class Operacao:
    def __call__(self, primeiro, segundo):
        raise NotImplementedError()


class Adicao(Operacao):
    def __call__(self, primeiro, segundo):
        return primeiro + segundo


class Calculadora:
    def __init__(self):
        self.operacoes = {'+': Adicao()}

    def adicionar_operacao(self, sinal, operacao):
        self.operacoes[sinal] = operacao

    def calcular(self, sinal, primeiro, segundo):
        operacao = self.operacoes[sinal]
        primeiro = float(primeiro)
        segundo = float(segundo)
        return operacao(primeiro, segundo)


# Usuário do framework

def subtracao(primeiro, segundo):
    return primeiro - segundo


if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.calcular('+', 3, 2))
    print(calculadora)
