''' Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar. No final, mostre:
 a) Qual é o total gasto na compra
 b) Quantos produtos custam mais de R$1000,00
 c) Qual o nome do produto mais barato '''

nomes = []
preços = []
totalGasto = 0
qtdValorMaiorMil = 0
menorValor = None
produtoMenorValor = None

while True:
    print(15*'=-=', '\nCadastro de Produto\n', 15*'=-=')
    nome = str(input('Insira o nome: '))
    nomes.append(nome)
    preço = float(input('Insira o valor: R$'))
    preços.append(preço)
    totalGasto += preço
    if preço > 1000:
        qtdValorMaiorMil += 1
    if produtoMenorValor == None:
        produtoMenorValor = nome
        menorValor = preço
    elif preço < menorValor:
        menorValor = preço
        produtoMenorValor = nome
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R${totalGasto:.2f}.')
print(f'{qtdValorMaiorMil} produtos têm seu valor maior que R$1000.00.')
print(f'O produto de menor valor é o/a {produtoMenorValor}, custando R${menorValor:.2f}.')