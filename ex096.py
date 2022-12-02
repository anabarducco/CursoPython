'''Faça um programa que tenha uma função chamada área, que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno. '''


def area(alt, larg):
    calculo_area = alt * larg
    print(f'A área do terreno de {alt}m * {larg}m é de {calculo_area:.1f}m².')


altura = float(input('Insira a altura do terreno retangular: '))
largura = float(input('Insira a largura do terreno retangular: '))
area(altura, largura)