''' Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7.00 por cada km acima do limite.'''

velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    valorMulta = (velocidade - 80) * 7
    print(f'Você foi multado! Sua multa ficou em R${valorMulta:.2f}.')
else:
    print('Você não foi multado. Siga em frente!')