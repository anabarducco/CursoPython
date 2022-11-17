''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o. '''

somaPares = 0
for i in range(0, 6):
    num = int(input(f'Insira o {i+1}º valor: '))
    if num % 2 == 0:
        somaPares += num
print(f'A soma dos números pares digitados é {somaPares}.')