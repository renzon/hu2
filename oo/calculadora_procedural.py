def calcular():
    primeiro = float(input('Digita o primeiro número: '))
    sinal = input('Digite a operação (+ ou -): ')
    segundo = float(input('Digita o segundo número: '))
    if sinal == '+':
        print(f'Resultado: {primeiro+segundo}')
    elif sinal == '-':
        print(f'Resultado: {primeiro-segundo}')
    else:
        raise Exception('Operação não implementada')


if __name__ == '__main__':
    calcular()
