''' Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. '''


def leiaint():
    while True:
        try:
            num = int(input('Insira um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[4;31mEste não é um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[4;31mDigitação interrompida pelo usuário.\033[m')
            return 0
        else:
            return int(num)


def leiafloat():
    while True:
        try:
            num = float(input('Insira um número real: '))
        except (ValueError, TypeError):
            print('\033[4;31mEste não é um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[4;31mDigitação interrompida pelo usuário.\033[m')
            return 0
        else:
            return float(num)


# programa principal
i = leiaint()
f = leiafloat()
print(f'Você digitou o número inteiro {i} e o número real {f}.')
