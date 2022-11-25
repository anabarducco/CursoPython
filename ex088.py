''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números, entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta. '''
import random
import time

jogos = list()

qtdJogos = int(input('Insira quantos jogos você deseja gerar: '))
for jogo in range(0, qtdJogos):
    palpite = list()
    while len(palpite) < 6:
        valor = random.randint(1, 61)
        if valor not in palpite:
            palpite.append(valor)
    jogos.append(palpite[:])

print(20*'--')
print(f'{"Os jogos gerados foram:":^40}')
for jogo in range(0, qtdJogos):
    print(20 * '--')
    time.sleep(1.0)
    print(f'Jogo {jogo+1}: ', sorted(jogos[jogo]))