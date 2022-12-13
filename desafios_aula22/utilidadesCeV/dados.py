def leiadinheiro():
    num = input('Insira o valor do produto: R$')
    num = num.replace(',', '.')
    verifica = num.replace('.', '')
    while not verifica.isdigit():
        print('\033[4;31mInválido. Digite um valor válido!\033[m')
        num = input('Insira o valor do produto: R$')
        num = num.replace(',', '.')
        verifica = num.replace('.', '')
    return float(num)

