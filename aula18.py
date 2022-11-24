''' Variáveis Compostas - LISTAS pt. 2
Listas dentro de listas - ex:
lista pessoas = cópia lista dados
pessoas[] = dados[] = [['Nome0', Idade0], ['Nome1', Idade1], ['Nome2', Idade2]]
pessoas[0] = ['Maria', 19]
pessoas[1] = ['Pedro', 25] etc
pessoas[0][0] = 'Maria'
pessoas[1][1] = 25
em listas, deve-se indicar os dados/campos com índices.
em dicionários, pode-se indicar com os respectivos nomes/identificadores '''

teste = list()
teste.append('Ana Beatriz')
teste.append(20)
print(teste)

galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'João'
teste[1] = 19
galera.append(teste[:])
print(galera)

outraGalera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(outraGalera)
print(outraGalera[0])
print(outraGalera[0][0])
print(outraGalera[2][1])
for pessoa in outraGalera:
    print(pessoa)
    print(pessoa[0], 'tem', end=' ')
    print(pessoa[1], 'anos de idade.')

maisGalera = list()
dado = list()
totalMaior = totalMenor = 0

for contagem in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    maisGalera.append(dado[:])
    dado.clear()
print(maisGalera)

for pessoa in maisGalera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totalMenor += 1
print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade.')