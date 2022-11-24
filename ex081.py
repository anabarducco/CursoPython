''' Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados
b) A lista de valores, ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista '''

lista = list()

while True:
    numero = lista.append(int(input('Insira um número inteiro: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break

print(40*'--')
print(f'Foram digitados {len(lista)} números.')
print(f'De forma decrescente, a lista fica: {sorted(lista, reverse=True)}.')

posicoes = list()

for numero in range(0, len(lista)):
    if lista[numero] == 5:
        posicoes.append(numero)

if len(posicoes) > 0:
    print(f'O número 5 foi digitado e aparece nas posições {posicoes}')
else:
    print('O número 5 não foi digitado.')