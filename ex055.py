''' Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. '''

pesos = []

for i in range(0, 5):
    pesoIndividual = float(input(f'Insira o peso da {i+1}ª pessoa, em kg: '))
    pesos.append(pesoIndividual)

maiorPeso = pesos[0]
menorPeso = pesos[0]

for i in range(1, 5):
    if pesos[i] > maiorPeso:
        maiorPeso = pesos[i]
    if pesos[i] < menorPeso:
        menorPeso = pesos[i]

print(f'O maior peso é {maiorPeso}kg e o menor peso é {menorPeso}kg.')