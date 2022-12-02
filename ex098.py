'''Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros:
início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada '''


def contador(inicio, fim, passo):
    print(f'Contador de {inicio} a {fim} com passo {passo}:')
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=' ')
            inicio += passo
    else:
        while fim <= inicio:
            print(inicio, end=' ')
            inicio -= passo
    print('Fim.')


contador(1, 10, 1)
contador(10, 0, 2)

pontoInicio = int(input('Valor Início: '))
pontoFinal = int(input('Valor Final: '))
passoContagem = int(input('Passo: '))

if passoContagem == 0:
    passoContagem = 1
elif passoContagem < 0:
    passoContagem *= (-1)

contador(pontoInicio, pontoFinal, passoContagem)