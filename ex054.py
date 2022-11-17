''' Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas
 ainda não atingiram a maioridade e quantas já são maiores.
 Considere a maioridade como 21 anos. '''

from datetime import date

anoAtual = date.today().year
maioridade = 0
menoridade = 0

for i in range(0, 7):
    anoNascimento = int(input(f'Insira o ano de nascimento da {i+1}ª pessoa: '))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(f'A quantidade de pessoas que já atingiram a maioridade é {maioridade}.\nE '
      f'a quantidade de pessoas que ainda são menores de idade é {menoridade}.')