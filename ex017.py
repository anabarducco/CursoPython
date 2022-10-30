#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimento da hipotenusa. a² = b² + c²

import math

catOposto = float(input('Insira o valor do cateto oposto: '))
catAdjacente = float(input('Insira o valor do cateto adjacente: '))

print(f'O valor da hipotenusa é {math.hypot(catOposto, catAdjacente):.2f}.')