#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos de alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Insira o nome do primeiro aluno: ')
aluno2 = input('Insira o nome do segundo aluno: ')
aluno3 = input('Insira o nome do terceiro aluno: ')
aluno4 = input('Insira o nome do quarto aluno: ')

listaAlunos = [aluno1, aluno2, aluno3, aluno4]

print(f'A ordem sorteada foi: {random.sample(listaAlunos, k=len(listaAlunos))}.')