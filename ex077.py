''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavras, quais são as suas vogais. '''

palavras = ('arvore', 'grama', 'flor', 'animais', 'pessoas', 'homem', 'mulher', 'criança')

for palavra in palavras:
    print(f'A palavra {palavra.upper()} tem as seguintes vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print('\n')