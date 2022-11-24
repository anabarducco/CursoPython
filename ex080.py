''' Crie mum programa onde o ousuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção, sem utilizar o sort().
No final, mostre a lista ordenada na tela. '''

lista = list()
for contagem in range(0, 5):
    valor = int(input('Digite um número inteiro: '))
    if contagem == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                break
            posicao += 1

print(20*'--', '\n', lista)