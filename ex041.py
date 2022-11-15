''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
 sua categoria, de acordo com a idade:
 Até 9 anos: mirim;
 Até 14 anos: infantil;
 Até 19 anos: junior;
 Até 20 anos: sênior;
 Acima: master. '''

from datetime import date

anoNascimento = int(input('Insira seu ano de nascimento: '))
idade = date.today().year - anoNascimento

if idade <= 9:
    print(f'Você tem {idade} anos está na categoria mirim.')
elif idade <= 14:
    print(f'Você tem {idade} anos está na categoria infantil.')
elif idade <= 19:
    print(f'Você tem {idade} anos está na categoria junior.')
elif idade <= 20:
    print(f'Você tem {idade} anos está na categoria senior.')
elif idade > 20:
    print(f'Você tem {idade} anos está na categoria master.')