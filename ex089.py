''' Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente. '''
import time

boletim = list()
dados = list()

while True:
    nome = str(input('Nome do aluno: ')).title()
    dados.append(nome)
    nota1 = float(input('Nota 1: '))
    dados.append(nota1)
    nota2 = float(input('Nota 2: '))
    dados.append(nota2)
    media = (nota1 + nota2)/2
    dados.append(media)
    boletim.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break

print(20*'--')
print(f'{"Boletim dos Alunos Cadastrados:":^40}')
print(20*'--')
print(f'{"ID":<5}{"Nome":<30}{"Média":^5}')
for aluno in range(0, len(boletim)):
    print(f'{aluno:<5}{boletim[aluno][0]:<30}{boletim[aluno][3]:<5.2f}')

while True:
    identificador = int(input('Insira o ID do aluno que deseja visualizar as notas ou 999 para encerrar: '))
    if identificador == 999:
        break
    print(20*'--')
    print('Notas do aluno ', f'\033[1m{boletim[identificador][0]}:\033[m')
    print('Nota 1: ', f'\033[1m{boletim[identificador][1]}\033[m')
    print('Nota 2: ', f'\033[1m{boletim[identificador][2]}\033[m')
    print('Média: ', f'\033[1m{boletim[identificador][3]}\033[m')
    print(20 * '--')
print('Encerrando o programa.')
time.sleep(1.0)