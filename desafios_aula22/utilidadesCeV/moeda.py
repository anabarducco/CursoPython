def dobro(num, formato=False):
    resultado = num * 2
    if formato:
        return moeda(resultado)
    else:
        return resultado


def metade(num, formato=False):
    resultado = num / 2
    if formato:
        return moeda(resultado)
    else:
        return resultado


def aumentar(num, formato=False):
    resultado = num * 1.10
    if formato:
        return moeda(resultado)
    else:
        return resultado


def diminuir(num, formato=False):
    resultado = num * 0.90
    if formato:
        return moeda(resultado)
    else:
        return resultado


def moeda(num):
    return f'R${num:.2f}'


def resumo(num):
    titulo('Resumo dos Valores')
    valores('Dobro', dobro(num, True))
    valores('Metade', metade(num, True))
    valores('Aumento de 10%', aumentar(num, True))
    valores('Desconto de 10%', diminuir(num, True))


def titulo(msg):
    print(20 * '--')
    print(f'{msg:^40}')
    print(20 * '--')


def valores(func, result):
    print(f'{func:.<30}', end='')
    print(f'{result:.>10}')

