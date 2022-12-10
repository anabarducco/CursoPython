''' Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do python,
 só que fazendo a validação para aceitar apenas um valor numérico. '''


def leiaint():
    num = input('Insira um número inteiro: ')
    while num.isnumeric() != True:
        print('\033[4;31mDigite um número válido.\033[m')
        num = input('Insira um número inteiro: ')
    return int(num)


#programa principal
n = leiaint()
print(f'Você digitou o número {n}.')