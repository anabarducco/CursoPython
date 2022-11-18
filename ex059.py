''' Crie um programa que leia dois valores e mostre um menu na tela:
 [1] somar
 [2] multiplicar
 [3] maior
 [4] novos números
 [5] sair do programa
 Seu programa deverá realizar a operação solicitada em cada caso. '''

import time

num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))

op = 0

while op != 5:
    print('Selecione a operação desejada de acordo com o menu a seguir:')
    op = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do Programa\n'))
    if op == 1:
        print(f'A soma dos valores {num1} e {num2} resulta em {num1+num2}.')
    elif op == 2:
        print(f'A multiplicação dos valores {num1} e {num2} resulta em {num1*num2}.')
    elif op == 3:
        if num1 > num2:
            print(f'O maior valor digitado foi {num1}.')
        else:
            print(f'O maior valor digitado foi {num2}.')
    elif op == 4:
        num1 = int(input('Insira o primeiro valor: '))
        num2 = int(input('Insira o segundo valor: '))
    elif op != 5:
        print('Escolha uma operação válida.')

print('Encerrando o programa.')
print(20*'==')
time.sleep(2.0)