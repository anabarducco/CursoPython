'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior. '''
import random
import time

numeros = []


def sorteia():
    print('Os números sorteados foram:')
    for contagem in range(0, 5):
        numeros.append(random.randint(1, 100))
    for valor in numeros:
        time.sleep(1.0)
        print(valor, end=' ')


def soma_par():
    somapar = 0
    print('Os números pares são:')
    for valor in numeros:
        if valor % 2 == 0:
            somapar += valor
            print(valor, end=' ')
    print(f'e a soma deles totaliza {somapar}.')


sorteia()
print()
soma_par()