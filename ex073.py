''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tabela está o time da Chapecoense. '''

tabelaCampeonato = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional',
                    'Cruzeiro', 'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia',
                    'Goiás', 'Guarani', 'Sport', 'Portuguesa', 'Atlético Paranaense', 'Vitória')

print(40*'--')
print('Os 5 primeiros times colocados no Campeonato Brasileiro de Futebol são: ')
for time in range(0, 5):
    print(f'{time+1}º: {tabelaCampeonato[time]}')

print(40*'--')
print('Os 4 últimos times colocados no Campeonato Brasileiro de Futebol são: ')
for time in range(19, 15, -1):
    print(f'{time+1}º: {tabelaCampeonato[time]}')

print(40*'--')
print(f'Os times colocados no Campeonato Brasileiro de Futebol em ordem alfabética são:\n{sorted(tabelaCampeonato)}')

print(40*'--')
time = 0
while time < 20:
    if tabelaCampeonato[time] == 'Chapecoense':
          print(f'O time da Chapecoense está na {time+1}ª posição.')
          break
    else:
        time += 1
if time == 20:
    print('O time da Chapecoense não foi classificada no Campeonato Brasileiro de Futebol neste ano!')
