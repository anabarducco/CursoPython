''' Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados, e também indique o menor e o maior valor gerados. '''

import random

numerosAleatorios = ()
#maiorNumero = None
#menorNumero = None

for i in range(0, 5):
    numeroAleatorio = random.randint(0, 100)
    numerosAleatorios += (numeroAleatorio, )
    #if maiorNumero == None:
    #    maiorNumero = numeroAleatorio
    #elif numeroAleatorio > maiorNumero:
    #    maiorNumero = numeroAleatorio
    #if menorNumero == None:
    #    menorNumero = numeroAleatorio
    #elif numeroAleatorio < menorNumero:
    #    menorNumero = numeroAleatorio

print(f'Os números gerados foram: {numerosAleatorios}.')
print(f'O maior número gerado foi {max(numerosAleatorios)} e o menor número gerado foi {min(numerosAleatorios)}.')