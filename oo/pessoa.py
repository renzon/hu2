class Pessoa:
    olhos = 2

    def __init__(self, nome='Renzo'):
        self.nome = nome


renzo = Pessoa()
renzo.sobrenome = 'Nuccitelli'
renzo.olhos = 3
print(renzo.__dict__)
print(Pessoa.olhos)
del renzo.olhos
print(renzo.__dict__)
print(renzo.olhos)
print(renzo.nome)
# print(Pessoa.nome)
