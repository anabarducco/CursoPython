''' Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. '''

listaUnica = [[], []]

for contagem in range(0, 7):
    numero = int(input(f'Digite o {contagem+1}º valor numérico: '))
    if numero % 2 == 0:
        listaUnica[0].append(numero)
    else:
        listaUnica[1].append(numero)

print(f'Valores pares: {sorted(listaUnica[0])}.')
print(f'Valores ímpares: {sorted(listaUnica[1])}.')