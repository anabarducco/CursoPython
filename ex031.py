''' Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km, e R$0.45 para viagens mais longas. '''

distancia = float(input('Insira a distância da viagem em Km: '))
if distancia <= 200:
    valorPassagem = distancia*0.50
else:
    valorPassagem = distancia*0.45

print(f'O valor da passagem é de R${valorPassagem:.2f}.')