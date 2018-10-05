class ProxyAtributosRealmentePrivados:
    def __init__(self, objeto=None):
        self.objeto = objeto

    def __getattr__(self, item:str):
        if item.startswith('_'):
            raise AttributeError('Acesso a atributo com _ não permitido')
        return getattr(self.objeto, item)
