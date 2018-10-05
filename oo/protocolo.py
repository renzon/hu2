class Servidor:
    def tratar_requisicao(self):
        if self._checar_permissoes():
            return self.executar_view()

    def _checar_permissoes(self):
        raise NotImplementedError()

    def executar_view(self):
        raise NotImplementedError


class ServidorSemChecagem(Servidor):
    def _checar_permissoes(self):
        return True

    def executar_view(self):
        return 'Sem checagem'


servidor = ServidorSemChecagem()
print(servidor.tratar_requisicao())
