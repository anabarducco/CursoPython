''' Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
 tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random

intAleatorio = random.randint(0,5)
intUsuario = int(input('Adivinhe qual número o computador pensou! '))

print(f'O computador escolheu o número {intAleatorio}.')

if intUsuario == intAleatorio:
    print('Parabéns, você venceu!')
else:
    print('Que pena, você perdeu!')