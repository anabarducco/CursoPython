#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus dígitos separados
#Ex: 1834 => unidade: 4; dezena: 3; centena: 8; milhar: 1.

numero = int(input('Insira um número de 0 a 9999: '))
unidade = numero//1 % 10
dezena = numero//10 % 10
centena = numero//100 % 10
milhar = numero//1000 % 10


'''if len(numero) == 1:
    print(f'Unidade = {numero[0]}')
if len(numero) == 2:
    print(f'Unidade = {numero[1]}\nDezena = {numero[0]}')
if len(numero) == 3:
    print(f'Unidade = {numero[2]}\nDezena = {numero[1]}\nCentena = {numero[0]}')
if len(numero) == 4:
    print(f'Unidade = {numero[3]}\nDezena = {numero[2]}\nCentena = {numero[1]}\nMilhar = {numero[0]}')'''

print(f'Unidade = {unidade}\nDezena = {dezena}\nCentena = {centena}\nMilhar = {milhar}')