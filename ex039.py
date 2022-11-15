''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
 Se ele ainda vai se alistar ao serviço militar;
 Se é a hora de se alistar;
 Se já passou do tempo de alistamento.

 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

from datetime import date

anoNascimento = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - anoNascimento

if idade < 18:
    print(f'Você deverá se alistar ao serviço militar em {18-idade} anos.')
elif idade == 18:
    print('Já é hora de se alistar!')
elif idade > 18:
    print(f'Você deveria ter se alistado ao serviço militar {idade-18} anos atrás.')