''' Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
 Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. '''
import time

valorCasa = float(input('Insira o valor da casa a ser comprada: '))
salarioComprador = float(input('Insira o salário do comprador: '))
anosPagando = int(input('Insira em quantos anos a cara será financiada: '))

prestacaoAnual = valorCasa/anosPagando
prestacaoMensal = prestacaoAnual/12

print(20*'====')
print('Processando pedido de empréstimo...')
print(20*'====')
time.sleep(2.0)

if prestacaoMensal > salarioComprador*0.3:
    print('Seu empréstimo bancário foi negado.')
    print(f'Em {anosPagando} anos, a prestação seria de {prestacaoMensal:.2f} e esse valor supera 30% do seu salário.')
else:
    print('Seu empréstimo bancário foi aprovado.')
    print(f'Em {anosPagando} anos, a prestação será de {prestacaoMensal:.2f}, '
          f'correspondendo a {prestacaoMensal/salarioComprador * 100:.2f}% do seu salário.')