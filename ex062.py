''' Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa se encerra quando ele disser que quer mostrar 0 termos. '''

import time

primeiroTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
qtdTermos = 10
ultimoTermo = primeiroTermo + (qtdTermos-1) * razao

print(primeiroTermo, end=' → ')
while primeiroTermo != ultimoTermo:
    primeiroTermo += razao
    print(primeiroTermo, end=' → ')
print('FIM\nOs 10 primeiros termos foram apresentados.')

while qtdTermos != 0:
    qtdTermos = int(input('Digite quantos termos a mais você deseja visualizar ou 0 para encerrar o programa: '))
    ultimoTermo = primeiroTermo + (qtdTermos) * razao
    while primeiroTermo != ultimoTermo:
        primeiroTermo += razao
        print(primeiroTermo, end=' → ')
    print(f'FIM\nOs {qtdTermos} termos foram apresentados.')
print(20*"=")
print('Encerrando o programa.')
time.sleep(2.0)