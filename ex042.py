''' Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
 Equilátero: todos os lados iguais;
 Isósceles: dois lados iguais;
 Escaleno: todos os lados diferentes. '''

reta1 = float(input('Insira o comprimento da primeira reta: '))
reta2 = float(input('Insira o comprimento da segunda reta: '))
reta3 = float(input('Insira o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo!')
    if reta1 == reta2 and reta2 == reta3:
        print('O triângulo formado é do tipo equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O triângulo formado é do tipo isósceles.')
    else:
        print('O triângulo formado é do tipo escaleno.')
else:
    print('Não é possível formar um triângulo.')