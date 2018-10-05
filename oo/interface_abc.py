import abc


class Servidor(abc.ABC):
    def tratar_requisicao(self):
        if self._checar_permissoes():
            return self.executar_view()

    @abc.abstractmethod
    def _checar_permissoes(self):
        pass

    @abc.abstractmethod
    def executar_view(self):
        pass


class ServidorSemChecagem(Servidor):
    def _checar_permissoes(self):
        return True

    def executar_view(self):
        return 'Sem checagem'


servidor = ServidorSemChecagem()
print(servidor.tratar_requisicao())
