''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de 0, o dicionário também receberá o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
Considere 35 anos de contribuição para a aposentadoria. '''

import datetime

pessoa = dict() #dicionário pessoa
anoAtual = datetime.date.today().year #função para saber qual o ano atual

pessoa['Nome'] = str(input('Nome: ')) #chave Nome - valor nome inserido
anoDeNascimento = int(input('Ano de Nascimento: ')) #pede o ano de nascimento
pessoa['Idade'] = anoAtual - anoDeNascimento #calcula a idade da pessoa de acordo com o ano de nascimento e o ano atual e guarda esse valor na chave Idade
pessoa['Carteira de Trabalho'] = int(input('Número Carteira de Trabalho: ')) #chave Carteira de Trabalho - valor número inserido
if pessoa['Carteira de Trabalho'] != 0:
    pessoa['Ano de Contratação'] = int(input('Ano de Contratação: ')) #chave ano de contratação = valor inserido
    anosTrabalhando = anoAtual - pessoa['Ano de Contratação']
    pessoa['Anos Faltantes para Aposentadoria'] = 35 - anosTrabalhando  # chave idade aposentadoria - valor calculado (35 - anos trabalhando)
    pessoa['Salário'] = float(input('Salário: ')) #chave salário - valor inserido

print(40*'--')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')