#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de
#tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m.

largura = float(input('Insira a largura da parede em metros: '))
altura = float(input('Insira a altura da parede em metros: '))
print(f'Essa parede tem {largura*altura} metros quadrados e necessita {(largura*altura)/2} litros de tinta para pintá-la.')