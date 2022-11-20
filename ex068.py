''' Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
 conquistou no jogo. '''

import random

numeroComputador = random.randint(0, 10)
totalVitorias = 0

print(15*'=-=', '\nPar ou Ímpar\n', 15*'=-=')

while True:
    numeroTotal = 0
    numeroJogador = int(input('Digite um número de 0 a 10: '))
    while True:
        escolhaJogador = str(input('Escolha par [P] ou ímpar [I]: ')).upper()
        if escolhaJogador in 'PI':
            break
    numeroTotal = numeroJogador + numeroComputador
    if numeroTotal % 2 == 0:
        if escolhaJogador == 'P':
            print(f'O computador escolheu {numeroComputador}.')
            print('Parabéns, você ganhou!')
            totalVitorias += 1
        else:
            print(f'O computador escolheu {numeroComputador}.')
            break
    else:
        if escolhaJogador == 'I':
            print(f'O computador escolheu {numeroComputador}.')
            print('Parabéns, você ganhou!')
            totalVitorias += 1
        else:
            print(f'O computador escolheu {numeroComputador}.')
            break
    print(15 * '=-=')
print(15 * '=-=')
print(f'Que pena, você perdeu!\nA quantidade de vitórias consecutivas foi de {totalVitorias}.')