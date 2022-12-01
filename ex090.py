''' Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela. '''

aluno = dict() #cria dicionário aluno
aluno['nome'] = str(input('Insira o nome do aluno: ')).title() #chave nome - valor nome inserido
aluno['média'] = float(input(f'Insira a média do aluno {aluno["nome"]}: ')) #chave média - valor média inserida
if aluno['média'] < 5.0: #verifica a situação do aluno
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Aprovado'

print(20*'--')
for key, value in aluno.items(): #printa a chave-valor inseridas no dicionário aluno
    print(f'{key}: {value}')