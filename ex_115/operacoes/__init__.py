from ex_115 import manipArquivos
import time


def leiaint():
    while True:
        try:
            num = int(input('Escolha uma opção: '))
        except (ValueError, TypeError):
            print('\033[4;31mEsta não é uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[4;31mDigitação interrompida pelo usuário.\033[m')
            return 0
        else:
            return int(num)


def opvalido(op):
    if op < 1 or op > 3:
        leiaint()
    elif op == 1:
        manipArquivos.cadastrar()
    elif op == 2:
        manipArquivos.listar()
    elif op == 3:
        print('Encerrando o sistema.')
        time.sleep(1.0)
        exit()
