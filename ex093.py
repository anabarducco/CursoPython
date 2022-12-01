''' Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitas em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. '''

jogador = dict()
gols = list()

jogador['Nome'] = str(input('Nome do Jogador: ')).title()
jogador['Quantidade de Partidas'] = int(input('Quantidade de Partidas Jogadas: '))

for contagem in range(0, jogador['Quantidade de Partidas']):
    golPartida = int(input(f'Quantidade de Gols na Partida {contagem+1}: '))
    gols.append(golPartida)
jogador['Quantidade Gols Partidas'] = gols
jogador['Quantidade Gols Campeonato'] = sum(gols)

print(40*'--')
print(jogador)
print(40*'--')
for chave, valor in jogador.items():
    print(f'O campo {chave} tem valor {valor}.')
print(40*'--')
print(f'O jogador {jogador["Nome"]} jogou {jogador["Quantidade de Partidas"]} partidas:')
contagem = 1
for gol in gols:
    print(f'    => Na {contagem}ª partida, fez {gol} gols.')
    contagem += 1
print(f'Foi um total de {jogador["Quantidade Gols Campeonato"]} gols.')
