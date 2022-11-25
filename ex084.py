''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves '''

dado = list()
copiaPesos = list()
pessoas = list()

while True:
    nomePessoa = str(input('Insira o nome da pessoa: '))
    dado.append(nomePessoa)
    pesoPessoa = float(input('Insira o peso da pessoa: '))
    dado.append(pesoPessoa)
    copiaPesos.append(pesoPessoa)
    pessoas.append(dado[:])
    dado.clear()
    continuar = str(input('Deseja continuar o cadastro? [S/N]: ')).upper()
    if continuar == 'N':
        break

nomesMaiorPeso = list()
nomesMenorPeso = list()
copiaPesos.sort()
for pessoa in pessoas:
    if pessoa[1] == copiaPesos[0]:
        nomesMenorPeso.append(pessoa[0])
    if pessoa[1] == copiaPesos[-1]:
        nomesMaiorPeso.append(pessoa[0])

print(f'Foram cadastradas {len(pessoas)} pessoas no total.')
print(f'O menor peso cadastrado foi {copiaPesos[0]}, e as pessoas cadastradas com esse peso foram {nomesMenorPeso}.')
print(f'O maior peso cadastrado foi {copiaPesos[-1]}, e as pessoas cadastradas com esse peso foram {nomesMaiorPeso}.')