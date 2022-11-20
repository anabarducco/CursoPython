''' Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999). '''

contagemNumeros = 0
somaNumeros = 0
print(15*'=-=', '\nContagem e soma de números\n', 15*'=-=')
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    contagemNumeros += 1
    somaNumeros += num
print(20*"=-=")
print(f'Foram digitados {contagemNumeros} números e a soma entre eles é {somaNumeros}.')