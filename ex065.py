''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
 todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer
 ou não continuar a digitar valores. '''

continuar = 'S'
soma = 0
qtdNumerosDigitados = 0
maiorValor = None
menorValor = None

while continuar == 'S':
    num = int(input('Insira um número inteiro: '))
    soma += num
    qtdNumerosDigitados += 1
    if maiorValor == None:
        maiorValor = num
    else:
        if num > maiorValor:
            maiorValor = num
    if menorValor == None:
        menorValor = num
    else:
        if num < menorValor:
            menorValor = num
    continuar = str(input('Deseja continuar digitando valores? [S/N] ')).upper()

mediaValores = soma/qtdNumerosDigitados

print(f'Foram digitados {qtdNumerosDigitados} números e a média de todos eles resulta em {mediaValores:.2f}.')
print(f'O maior valor digitado foi {maiorValor} e o menor valor digitado foi {menorValor}.')