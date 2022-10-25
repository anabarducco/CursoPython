#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

anguloGrau = int(input('Insira o valor do ângulo em graus: '))
anguloRad = math.radians(anguloGrau)

senoRad = math.sin(anguloRad)
cosRad = math.cos(anguloRad)
tanRad = math.tan(anguloRad)

print(f'O valor do seu seno é {senoRad:.3f}, do seu cosseno é {cosRad:.3f} e da sua tangente é {tanRad:.3f}.')