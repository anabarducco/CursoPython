''' Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
 elementos de uma Sequência de Fibonacci. '''

num = int(input('Insira um número inteiro: '))

ultimo = 1
penultimo = 0

if num == 1:
    print(f'1 → FIM')
else:
    inicio = 2
    print(f'1 → ', end='')
    while inicio <= num:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        inicio += 1
        print(f'{termo} → ', end='')
    print('FIM')