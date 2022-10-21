#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Insira um número inteiro: '))
print(f'A tabuada de {num} é:')
i = 1
while i<=10:
    print(num*i)
    i+=1
