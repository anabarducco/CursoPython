''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
 digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o 999. '''

num = 0
soma = 0
qtdNumerosDigitados = 0

while num != 999:
    num = int(input('Insira um número inteiro ou 999 para encerrar o programa: '))
    if num != 999:
        soma += num
        qtdNumerosDigitados += 1

print(f'Foram digitados {qtdNumerosDigitados} números e a soma de todos eles resulta em {soma}.')