''' Desenvolva um programa que leia o nome, idade e gênero de 4 pessoas. No final do programa, mostre:
 A média de idade do grupo;
 Qual é o nome do homem mais velho;
 Quantas mulheres têm menos de 20 anos. '''

nomes = []
idades = []
generos = []

#lendo todos os dados das 4 pessoas
for i in range(0, 4):
    nomeIndividual = str(input(f'Insira o nome da {i+1}ª pessoa: '))
    nomes.append(nomeIndividual)
    idadeIndividual = int(input(f'Insira a idade da {i + 1}ª pessoa: '))
    idades.append(idadeIndividual)
    generoIndividual = int(input(f'Selecione o gênero da {i + 1}ª pessoa:\n[1] Mulher\n[2] Homem\n'))
    generos.append(generoIndividual)

#cálculo da média de idade
somaIdades = 0
for i in range(0, 4):
    somaIdades += idades[i]
mediaIdades = somaIdades/4

#identificando quem é o homem mais velho
maiorIdade = 0
nomeHomemMaisVelho = 'nenhum - não existe homem mais velho.'
for i in range(0, 4):
    if generos[i] == 2:
        if idades[i] > maiorIdade:
            maiorIdade = idades[i]
            nomeHomemMaisVelho = nomes[i]

#cálculo da quantidade de mulheres com menos de 20 anos
mulheresMenosVinteAnos = 0
for i in range(0, 4):
    if generos[i] == 1:
        if idades[i] < 20:
            mulheresMenosVinteAnos += 1

print(f'A média de idade do grupo é {mediaIdades:.1f} anos.')
print(f'O nome do homem mais velho do grupo é {nomeHomemMaisVelho}.')
print(f'A quantidade de mulheres com menos de 20 anos neste grupo é {mulheresMenosVinteAnos}.')