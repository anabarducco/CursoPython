''' Crie um programa que faça o computador jogar Jokenpô com você. '''

import random

listaJokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaComputador = random.choice(listaJokenpo)
escolhaUsuario = str(input('Escolha entre pedra, papel e tesoura.\nR: '))
escolhaUsuario = escolhaUsuario.upper()

if escolhaUsuario == escolhaComputador:
    print('O jogo empatou!')
elif escolhaUsuario == 'PEDRA' and escolhaComputador == 'PAPEL':
    print('O ganhador foi o computador!')
elif escolhaUsuario == 'PEDRA' and escolhaComputador == 'TESOURA':
    print('O ganhador foi o usuário!')
elif escolhaUsuario == 'PAPEL' and escolhaComputador == 'PEDRA':
    print('O ganhador foi o usuário!')
elif escolhaUsuario == 'PAPEL' and escolhaComputador == 'TESOURA':
    print('O ganhador foi o computador!')
elif escolhaUsuario == 'TESOURA' and escolhaComputador == 'PEDRA':
    print('O ganhador foi o computador!')
elif escolhaUsuario == 'TESOURA' and escolhaComputador == 'PAPEL':
    print('O ganhador foi o usuário!')
else:
    print('Escolha uma opção válida para jogar!')

print(f'As escolhas foram:\nUsuário: {escolhaUsuario}\nComputador: {escolhaComputador}')