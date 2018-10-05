from time import strftime


class Servidor():
    def tratar_request(self):
        print("Tratando Request")


class ServidorComLog(Servidor):
    def tratar_request(self):
        print(strftime('%H:%M:%S'))
        super().tratar_request()


ServidorComLog().tratar_request()
