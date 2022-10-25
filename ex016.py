#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: entrada 6.127; saída 6.

import math

num = float(input('Insira um número qualquer: '))
print(f'Sua porção inteira é {math.trunc(num)}.')