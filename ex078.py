''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista. '''

lista = list()
for contagem in range(0, 5):
    lista.append(int(input('Digite um número inteiro: ')))

posicoesMax = list()
posicoesMin = list()

for numero in range(0, len(lista)):
    if lista[numero] == max(lista):
        posicoesMax.append(numero)
    if lista[numero] == min(lista):
        posicoesMin.append(numero)

print(20*'--', f'\nVocê digitou os números {lista}\n', 20*'--')
print(f'O maior valor digitado foi {max(lista)} nas posições {posicoesMax}.\n'
      f'O menor valor digitado foi {min(lista)} nas posições {posicoesMin}.')