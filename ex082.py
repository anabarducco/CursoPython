''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
No final, mostre o conteúdo das três listas geradas. '''

listaCompleta = list()
listaPares = list()
listaImpares = list()

while True:
    numero = listaCompleta.append(int(input('Insira um número inteiro: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break

for contador in range(0, len(listaCompleta)):
    if listaCompleta[contador] % 2 == 0:
        listaPares.append(listaCompleta[contador])
    else:
        listaImpares.append(listaCompleta[contador])

print(f'A lista completa digitada foi: {listaCompleta}')
print(f'A lista dos números pares digitados foi: {listaPares}')
print(f'A lista dos números ímpares digitados foi: {listaImpares}')