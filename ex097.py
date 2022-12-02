'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex: escreva('Olá Mundo!')
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
'''


def escreva(txt):
    tamanho_texto = len(txt) + 4
    print(tamanho_texto*'~')
    print(f'  {txt}  ')
    print(tamanho_texto*'~')


escreva('Ana Beatriz')
escreva('Olá, Mundo!')
frase = str(input('Escreva uma frase qualquer: '))
escreva(frase)