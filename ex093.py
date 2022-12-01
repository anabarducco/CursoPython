''' Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitas em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. '''

jogador = dict()
qtdGols = 0

jogador['Nome'] = str(input('Nome do Jogador: ')).title()
jogador['Quantidade de Partidas'] = int(input('Quantidade de Partidas Jogadas: '))

for contagem in range(0, jogador['Quantidade de Partidas']):
    jogador[f'Quantidade Gols Partida {contagem+1}'] = int(input(f'Quantidade de Gols na Partida {contagem+1}: '))
    qtdGols += jogador[f'Quantidade Gols Partida {contagem+1}']
jogador['Quantidade Gols Campeonato'] = qtdGols

print(20*'--')
for chave, valor in jogador.items():
    print(f'{chave}: {valor}')