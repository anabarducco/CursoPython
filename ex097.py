'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex: escreva('Olá Mundo!')
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
'''


def escreva(txt):
    tamanho_texto = len(txt)
    print(tamanho_texto*'~')
    print(txt)
    print(tamanho_texto*'~')


frase = str(input('Escreva uma frase qualquer: '))
escreva(frase)