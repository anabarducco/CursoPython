''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) A média de idade do grupo;
c) Uma lista com todas as mulheres;
d) Uma lista com todas as pessoas com idade acima da média. '''

pessoas = list() #lista pessoas
pessoa = dict() #dicionário com dados de cada pessoa
somaIdade = 0

while True: #até o usuário decidir parar
    pessoa['Nome'] = str(input('Nome: ')).title() #chave nome - valor inserido
    pessoa['Sexo'] = str(input('Sexo [F/M]: ')).upper() #chave sexo - valor inserido
    while pessoa['Sexo'] not in 'FM': #confere se o valor inserido é valido
        pessoa['Sexo'] = str(input('Sexo [F/M]: ')).upper()
    pessoa['Idade'] = int(input('Idade: ')) #chave idade - valor inserido
    somaIdade += pessoa['Idade'] #soma a idade de todas as pessoas cadastradas
    pessoas.append(pessoa.copy()) #copia p/ lista o dicionário atual (com os dados da pessoa)
    pessoa.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper() #verifica se a pessoa deseja continuar o cadastro
    if continuar == 'N': #verificação de parada do while
        break

mediaIdade = somaIdade/len(pessoas) #calcula a média de idade das pessoas cadastradas

print(20*'--')
print(f'Foram criadas {len(pessoas)} pessoas.')
print(f'A média de idade das pessoas cadastradas é {mediaIdade:.1f}.')
print('As mulheres cadastradas foram: ')
for pes in pessoas: #para cada pessoa da lista
    if pes['Sexo'] == 'F': #se a pessoa for do sexo feminino
        print(pes['Nome']) #printa o nome da pessoa
print('As pessoas cadastradas com idade acima da média foram: ')
for pes in pessoas: #para cada pessoa da lista
    if pes['Idade'] > mediaIdade: #se a idade da pessoa for maior que a da média
        print(pes['Nome']) #printa o nome da pessoa