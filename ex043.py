''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o status, de acordo
 com a tabela abaixo:
 Abaixo de 18.5: abaixo do peso;
 Até 25: peso ideal;
 Até 30: sobrepeso;
 Até 40: obesidade;
 Acima de 40: obesidade mórbida. '''

peso = float(input('Insira seu peso em quilos: '))
altura = float(input('Insira sua altura em metros: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Seu IMC é de {imc:.2f} e você está abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f} e você está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f} e você está em sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f} e você está obeso.')
elif imc > 40:
    print(f'Seu IMC é de {imc:.2f} e você está obeso mórbido.')