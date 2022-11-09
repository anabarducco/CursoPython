''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor. '''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 >= num2 and num1 >= num3:
    maiorNum = num1
else:
    if num2 >= num1 and num2 >= num3:
        maiorNum = num2
    else:
        maiorNum = num3

if num1 <= num2 and num1 <= num3:
    menorNum = num1
else:
    if num2 <= num1 and num2 <= num3:
        menorNum = num2
    else:
        menorNum = num3

print(f'O maior número é {maiorNum} e o menor número é o {menorNum}.')