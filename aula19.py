'''  Variáveis Compostas - Dicionários
Estrutura de dados similar a tuplas e listas, mas com índices literais
Identificados por dados = {} ou dados = dict()
dados{'nome': 'Ana', 'idade': 20}
print(dados['nome'])
pra adicionar: declarar dados['algo']='algo'
pra remover: del dados['algo']
-
valores, chaves e itens
valores/ values(): valores inseridos nas variáveis (ex: 'Ana', 20)
chaves/ keys(): nomes dados aos índices (ex: 'nome', 'idade')
itens/ items(): índices e valores respectivos (ex: 'nome', 'Ana') => utilizado em FOR, como com enumerate
    for key, values in dados.items():
        print(f'O {key} é {value}.')
-
É possível mesclar dicionários com listas (ex: lista Locadora com dicionários de Filmes, com título, ano e diretor)'''

pessoas = {'nome': 'Ana', 'sexo': 'F', 'idade': 20}
print(pessoas)
print(f'A {pessoas["nome"]}, do sexo {pessoas["sexo"]}, tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for key in pessoas.keys():
    print(key)
for value in pessoas.values():
    print(value)
for item in pessoas.items():
    print(item)
for key, value in pessoas.items():
    print(f'{key} = {value}')
del pessoas["sexo"]
print(pessoas)
pessoas["nome"] = 'Ana Beatriz'
print(pessoas)

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = list()
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])

estado = dict()
br = list()
for contagem in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    br.append(estado.copy())
print(br)
for es in br:
    for key, value in es.items():
        print(f'O campo {key} tem valor {value}.')