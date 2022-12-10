''' Faça um programa que tenha uma função chamada nota() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:
a) Quantidade de notas;
b) A maior nota;
c) A menor nota;
d) A média da turma;
e) A situação (opcional).
Adicione também as docstrings da função. '''


def nota(*notas, situ=False):
    """
    -> A função nota recebe várias notas e retorna a quantidade de notas recebidas, a maior e a menor, a média das notas
    e a situação do aluno, se a pessoa optar por ver
    :param notas: dicionário de notas inseridas
    :param situ: opcional se a pessoa deseja ver ou não a situação do aluno (ruim/média/boa/excelente)
    :return: quantidade de notas recebidas, a maior e a menor, a média das notas e a situação do aluno (opcional)
    """
    somaNotas = 0
    for nota in notas:
        somaNotas += nota
    mediaNotas = somaNotas/len(notas)
    if mediaNotas < 5:
        situacao = 'Ruim'
    elif 5 <= mediaNotas < 7:
        situacao = 'Média'
    elif 7 <= mediaNotas < 9:
        situacao = 'Boa'
    else:
        situacao = 'Excelente'
    if situ == True:
        print(f'Foram digitadas {len(notas)} notas. A maior foi {max(notas)} e a menor foi {min(notas)}.'
              f' A média das notas é {mediaNotas:.2f} e a situação é {situacao}.')
    else:
        print(f'Foram digitadas {len(notas)} notas. A maior foi {max(notas)} e a menor foi {min(notas)}. '
              f'A média das notas é {mediaNotas:.2f}.')


#programa principal
dicNotas = ()
while True:
    notaAvulsa = float(input('Insira a nota do aluno: '))
    dicNotas += (notaAvulsa, )
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
situTurma = str(input('Deseja ver a situação do aluno? [S/N]: ')).upper()
while situTurma not in 'SN':
    situTurma = str(input('Deseja ver a situação do aluno? [S/N]: ')).upper()
if situTurma == 'S':
    nota(*dicNotas, situ=True)
else:
    nota(*dicNotas)