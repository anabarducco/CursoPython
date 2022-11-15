''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
 1 para binário;
 2 para octal;
 3 para hexadecimal. '''



num = int(input('Insira um número inteiro: '))
op = int(input('Digite 1 para convertê-lo em binário\nDigite 2 para convertê-lo em octal\nDigite 3 para convertê-lo em hexadecimal\n'))

if op == 1:
    print(f'{bin(num)[2:]}')
elif op == 2:
    print(f'{oct(num)[2:]}')
elif op == 3:
    print(f'{hex(num)[2:]}')
else:
    print('A opção escolhida não existe.')