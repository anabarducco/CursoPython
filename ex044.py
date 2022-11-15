''' Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e a
 condição de pagamento:

 À vista dinheiro/cheque: 10% de desconto;
 À vista no cartão: 5% de desconto;
 Até 2x no cartão: preço normal;
 3x ou mais no cartão: 20% de juros. '''
import time

valorProduto = float(input('Insira o valor normal do produto: R$'))
formaPgto = int(input('Escolha a forma de pagamento:\n1 - À vista no dinheiro ou cheque\n'
                      '2 - À vista no cartão\n3 - Parcelado em até 2x no cartão\n'
                      '4 - Parcelado em 3x ou mais no cartão\n'))

print(20*'====')
print('PROCESSANDO...')
print(20*'====')
time.sleep(3.0)

if formaPgto == 1:
    print(f'O valor a ser pago no total é de R${valorProduto - (valorProduto*0.1):.2f}')
elif formaPgto == 2:
    print(f'O valor a ser pago no total é de R${valorProduto - (valorProduto*0.05):.2f}')
elif formaPgto == 3:
    print(f'O valor a ser pago no total é de R${valorProduto:.2f}')
elif formaPgto == 4:
    print(f'O valor a ser pago no total é de R${valorProduto + (valorProduto*0.2):.2f}')
else:
    print('A opção escolhida não existe.')