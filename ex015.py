#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

km = float(input('Quantos km foram percorridos com o carro? '))
dias = int(input('Quantos dias o carro foi alugado? '))

totalKm = km*0.15
totalDias = dias*60
totalFinal = totalKm + totalDias

print(f'O valor total a ser pago é R${totalFinal:.2f}.')