''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
 Valor literal = frase
 até 15: não vota/ 16-17: opcional/ 18-65: obrigatório/ +65: opcional '''
from datetime import datetime


def voto(anoNascimento):
    anoAtual = datetime.now().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return f'Você tem {idade} anos e sua situação nas eleições é: VOTO NEGADO.'
    elif 16 <= idade <= 17:
        return f'Você tem {idade} anos e sua situação nas eleições é: VOTO OPCIONAL.'
    elif 18 <= idade <= 65:
        return f'Você tem {idade} anos e sua situação nas eleições é: VOTO OBRIGATÓRIO.'
    else:
        return f'Você tem {idade} anos e sua situação nas eleições é: VOTO OPCIONAL.'


anoNasc = int(input('Insira seu ano de nascimento: '))
print(voto(anoNasc))