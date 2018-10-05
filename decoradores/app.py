from decoradores.flask import rota

@rota('/')
def raiz():
    return 'Home'

print(raiz())