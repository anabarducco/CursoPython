''' Crie um programa que simule o funcionamento de um caixa eletrônico.
 No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
 informar quantas cédulas de cada valor serão entregues.
 OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1 '''

qtdCinquenta = 0
qtdVinte = 0
qtdDez = 0
qtdUm = 0

print(15*'--', '\nCaixa Eletrônico\n', 15*'--')
print('Para o saque, temos disponíveis cédulas nos seguintes valores:\nR$50\nR$20\nR$10\nR$1')
valorSaque = int(input('Insira o valor a ser sacado: '))

while True:
    while valorSaque - 50 >= 0:
        qtdCinquenta += 1
        valorSaque -= 50
    while valorSaque - 20 >= 0:
        qtdVinte += 1
        valorSaque -= 20
    while valorSaque - 10 >= 0:
        qtdDez += 1
        valorSaque -= 10
    while valorSaque - 1 >= 0:
        qtdUm += 1
        valorSaque -= 1
    if valorSaque == 0:
        break
print(f'No saque, você receberá {qtdCinquenta} notas de R$50.00, {qtdVinte} notas de R$20.00, '
      f'{qtdDez} notas de R$10.00 e {qtdUm} notas de R$1.00.')