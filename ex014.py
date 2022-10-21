#Escreva um programa que converta uma temperatura digitada em ºC e a converta para ºF.

tempC = float(input('Escreva a temperatura em ºC: '))
tempF = (tempC * 9/5) + 32

print(f'Essa temperatura equivale a {tempF:.1f} ºF.')