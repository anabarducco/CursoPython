#Adaptado
#Crie um programa que leia dois números e mostre as possíveis operações aritméticas entre eles

n1 = float(input('Insira um número: '))
n2 = float(input('Insira um número: '))
soma = n1+n2
subt = n1-n2
mult = n1*n2
div = n1/n2

print(f'{n1} + {n2} = {soma}')
print(f'{n1} - {n2} = {subt}')
print(f'{n1} * {n2} = {mult}')
print(f'{n1} / {n2} = {div}')