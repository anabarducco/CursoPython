''' Crie um programa que tenha uma função fatorial() que receba 2 parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial. '''


def fatorial(num, show=False):
    """
    -> A função fatorial calcula o fatorial do parâmetro num passado, podendo mostrar, ou não, o processo de cálculo.
    :param num: número que terá seu fatorial calculado
    :param show: (opcional) parâmetro que define se será mostrado o processo de cálculo (True= sim/ False= não)
    :return: o valor fatorial calculado
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            if c != 1:
                print(c, 'x', end=' ')
            else:
                print(c, '=', end=' ')
    return f


numero = int(input('Insira um número para calcular seu fatorial: '))
while True:
    mostrarProcesso = str(input('Você deseja ver o processo de cálculo? [S/N]: ')).upper()
    if mostrarProcesso not in 'SN':
        print('Por favor, digite um valor válido.')
    if mostrarProcesso == 'S':
        print(fatorial(numero, True))
        break
    else:
        print(fatorial(numero))
        break

#print(help(fatorial))