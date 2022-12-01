''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. '''

import random
import time

resultados = dict() #cria dicionário resultados

print(20*'--')
print('Os resultados obtidos por cada jogador foram:')
for contagem in range(0, 4): #para 4 jogadores
    resultados[f'Jogador{contagem+1}'] = random.randint(1, 7) #cria chave jogador[contagem] - valor número aleatório gerado
print(resultados) #printa o dicionário
print(20*'--')
print('A colocação de acordo com o resultado obtido fica: ')
for resultado in sorted(resultados, key = resultados.get, reverse=True): #para cada resultado no dicionário resultados, ordena os valores gerados do maior para o menor
    time.sleep(1.0)
    print(resultado,': ', resultados[resultado])