''' Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formam um triângulo. '''

reta1 = float(input('Insira o comprimento da primeira reta: '))
reta2 = float(input('Insira o comprimento da segunda reta: '))
reta3 = float(input('Insira o comprimento da terceira reta: '))

if reta1 < reta2:
    menorReta1 = reta1
    if reta2 < reta3:
        menorReta2 = reta2
        maiorReta = reta3
    else:
        menorReta2 = reta3
        maiorReta = reta2
else:
    menorReta1 = reta2
    if reta1 < reta3:
        menorReta2 = reta1
        maiorReta = reta3
    else:
        menorReta2 = reta3
        maiorReta = reta1

if menorReta1 + menorReta2 > maiorReta:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')