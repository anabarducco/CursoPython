''' Faça um programa que leia um ano qualquer e mostre se ele é bissexto '''

import calendar

ano = int(input('Insira um ano qualquer: '))
bissexto = calendar.isleap(ano)
if bissexto == True:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')