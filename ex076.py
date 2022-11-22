''' Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular. '''

from tabulate import tabulate

produtos = ('Lápis', 0.50,
            'Caneta Azul', 1.00,
            'Caneta Vermelha', 1.50,
            'Caneta Preta', 1.25,
            'Kit 6 Canetas Coloridas', 12.50,
            'Caderno 96 Folhas', 25.99,
            'Caderno 150 Folhas', 36.90,
            'Kit 4 Grifa-Textos', 21.00,
            'Bloco Post-It', 8.50,
            'Mochila', 175.00)
print(20*'--')
print(f'{"Listagem de Preços":^40}')
print(20*'--')
for produto in range(0, len(produtos)-1, 2):
    print(f'{produtos[produto]:.<30}R${produtos[produto+1]:>7.2f}')
print(20*'--')