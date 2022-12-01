''' Aprimore o exercício 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador. '''

jogador = dict() #dicionário de cada jogador
jogadores = list() #lista com todos os jogadores

while True: #enquanto o usuário quiser cadastrar
    qtdGols = 0 #qtdGols sempre volta a 0
    jogador["Nome"] = str(input('Nome do Jogador: ')).title() #chave nome - valor inserido
    jogador["Quantidade de Partidas"] = int(input('Quantidade de Partidas Jogadas: ')) #chave qtd partidas - valor inserido
    for contagem in range(0, jogador["Quantidade de Partidas"]): #para cada partida cadastra a qtd de gols
        jogador[f"Quantidade Gols Partida {contagem+1}"] = int(input(f'Quantidade de Gols na Partida {contagem+1}: '))
        qtdGols += jogador[f"Quantidade Gols Partida {contagem+1}"] #calcula a qtd de gols totais do campeonato
    jogador["Quantidade Gols Campeonato"] = qtdGols #chave qtd gols campeonato - valor calculado em qtdGols
    jogadores.append(jogador.copy()) #copia os dados do dicionário para a lista
    jogador.clear() #limpa os dados do dicionário
    continuar = str(input('Deseja continuar? [S/N]: ')).upper() #verifica se o usuário deseja continuar
    if continuar == 'N': #condição de parada
        break

print(20*'--')
print(f'{"ID":<4}|{"Nome":^20}|{"Quantidade de Partidas":^25}|{"Quantidade Gols Campeonato":^40}')
for jog in jogadores:
    print(f'{jogadores.index(jog):<4}|{jog["Nome"]:<20}|{jog["Quantidade de Partidas"]:^25}'
          f'|{jog["Quantidade Gols Campeonato"]:^40}')

while True:
    print(20 * '--')
    id = int(input('Digite o ID do jogador para ver os detalhes de cada partida ou 999 para encerrar o programa: '))
    if id == 999:
        break
    print(f'Detalhes das partidas jogadas pelo jogador {jogadores[id]["Nome"]}:')
    print(f'{"Partida":^10}|{"Quantidade Gols":^20}')
    # preciso fazer o sistema de visualização de detalhes de cada partida de cada jogador