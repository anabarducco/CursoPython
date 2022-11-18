''' Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando quantos palpites foram necessários para vencer. '''

import random

intAleatorio = random.randint(0, 10)
intUsuario = int(input('Adivinhe qual número entre 0 e 10 o computador pensou! '))

palpites = 1

while intUsuario != intAleatorio:
    if intUsuario < intAleatorio:
        intUsuario = int(input('Você errou! O número que o computador pensou é maior... Tente novamente: '))
        palpites += 1
    elif intUsuario > intAleatorio:
        intUsuario = int(input('Você errou! O número que o computador pensou é menor... Tente novamente: '))
        palpites += 1

print(f'Parabéns, você acertou após {palpites} palpites!')