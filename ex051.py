''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão. '''

primeiroTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimoTermo = primeiroTermo + (10-1) * razao

for i in range(primeiroTermo, decimoTermo + razao, razao):
    print(i, end=' → ')
print('FIM')