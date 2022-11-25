''' Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. '''

listaUnica = list()
par = list()
impar = list()

for contagem in range(0, 7):
    numero = int(input(f'Digite o {contagem+1}º valor numérico: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
impar.sort()

listaUnica.append(par[:])
listaUnica.append(impar[:])

print(f'Valores pares: {listaUnica[0]}.')
print(f'Valores ímpares: {listaUnica[1]}.')