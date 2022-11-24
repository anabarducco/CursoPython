''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

lista = list()
while True:
    valor = int(input('Digite um número inteiro: '))
    if valor in lista:
        print('Esse número já está na lista. Ele não foi adicionado.')
    else:
        lista.append(valor)
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print(20*'--', f'\nOs valores digitados foram {sorted(lista) }.')