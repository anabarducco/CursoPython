''' Faça um programa que leia um número qualquer e mostre o seu fatorial. '''

num = int(input('Insira um número inteiro: '))
numero = num

fatorial = 1

while num > 0:
    fatorial *= num
    num -= 1

print(f'{numero}! = {fatorial}')