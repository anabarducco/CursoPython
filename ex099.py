''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior. '''


def maior(*num):
    print(f'Os valores passados foram: {num}')
    print(f'Destes {len(num)} valores, o maior é {max(num)}.')


maior(1, 2, 3)
maior(10, 95, 15, 47, 36)
maior(-1, -5, -17)

numeros = ()
while True:
    valor = int(input('Insira um número inteiro: '))
    numeros += (valor,)
    cont = str(input('Deseja continuar? [S/N]: ')).upper()
    if cont == 'N':
        break

maior(*numeros) #forma correta de passar os valores da tupla, e não a tupla como valor