''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''

primo = True

num = int(input('Insira um número inteiro: '))

for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo == True:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')