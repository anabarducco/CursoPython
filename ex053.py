''' Faça um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. '''

frase = str(input('Insira uma frase: ')).strip().upper()
fraseSemEspaço = frase.replace(' ', '')
tamanhoFrase = len(fraseSemEspaço) - 1

checagem = 0
limite = tamanhoFrase

for i in range(0, limite):
    if fraseSemEspaço[i] == fraseSemEspaço[limite]:
        limite -= 1
        checagem += 1

if checagem == tamanhoFrase:
    print('A frase escrita é um palíndromo.')
else:
    print('A frase escrita não é um palíndromo.')

# É possível fazer utilizando fatiamento. Bastaria colocar:
# fraseInvertida = fraseSemEspaço[::-1] => vai pegar a frase sem espaço de trás pra frente
# e depois faz um if comparando fraseSemEspaço e fraseInvertida. Se forem iguais, é palíndromo.