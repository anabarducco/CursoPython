''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 até 20.
 Seu programa deverá ler um número pelo teclado, entre 0 e 20, e mostrá-lo por extenso. '''

from num2words import num2words

numerosExtensos = ()

for numero in range(0, 21):
    numeroExtenso = num2words(numero, lang='pt-br')
    numerosExtensos += (numeroExtenso, )

while True:
    lerNumero = int(input('Insira um número de 0 a 20: '))
    if 0 <= lerNumero <= 20:
        print(f'O número {lerNumero} por extenso se escreve {numerosExtensos[lerNumero]}.')
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
        if continuar == 'N':
            break