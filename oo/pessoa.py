
class Pessoa:
    olhos = 2

    olhos+=1

    def __init__(self, nome='Renzo', idade=36):
        self._idade = idade
        self.nome = nome



    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor<0:
            raise ValueError('Valor não pode ser negativo')
        self._idade = valor

    def __str__(self):
        return f'{self.nome}: {self.idade}'

    def __getattribute__(self, item:str):
        print(item)
        if item.startswith('_'):
            raise AttributeError('Acesso a atributo com _ não permitido')
        return getattr(self, item)



renzo = Pessoa()

# renzo.idade = -1
renzo.idade = 1
# print(renzo._idade)
print(renzo.lkhsgdflkasfd)
print(renzo.idade)
print(renzo)

# renzo.sobrenome = 'Nuccitelli'

# renzo.olhos = 3
# print(renzo.__dict__)
# print(Pessoa.olhos)
# del renzo.olhos
# print(renzo.__dict__)
# print(renzo.olhos)
# print(renzo.nome)
# print(Pessoa.nome)
