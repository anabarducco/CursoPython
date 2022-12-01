''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. '''

import random
import time

resultados = dict() #cria dicionário resultados
for contagem in range(1, 5): #para 4 jogadores
    resultados[f'Jogador{contagem}'] = random.randint(1, 6) #cria chave jogador[contagem] - valor número aleatório gerado

print(20 * '--')
print('Os resultados obtidos por cada jogador foram:')
for chave, valor in resultados.items():
    time.sleep(1.0)
    print(f'{chave} tirou {valor} no dado.') #printa a chave (jogador) e o valor (número do dado)

print(20*'--')
print('Ranking dos Jogadores: ')
contagem = 1
for resultado in sorted(resultados, key = resultados.get, reverse=True): #para cada resultado no dicionário resultados, ordena os valores gerados do maior para o menor
    time.sleep(1.0)
    print(f'{contagem}º Lugar: {resultado} - {resultados[resultado]}') #printa o ranking com colocação, jogador e valor do dado
    contagem += 1