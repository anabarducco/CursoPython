''' Faça um mini sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: Use cores. '''

cores = (
    '\033[m', #0 - sem cor
    '\033[0;30;45m', #1 - fundo roxo com texto branco
    '\033[0;34;40m', #2 - invertido, fundo branco com texto azul
    '\033[0;30;41m', #3 - fundo vermelho com texto branco
    '\033[0;30;42m', #4 - fundo verde com texto branco
    '\033[0;30;43m', #5 - fundo amarelo com texto branco
)


def interactivehelp(comando):
    titulo(comando, cor=1)
    texto(comando, cor=2)


def separador(tamanho):
    print(tamanho*'~')


def titulo(msg, cor=0):
    tam = len(msg)
    print(cores[cor], end='')
    separador(tam)
    print(msg)
    separador(tam)
    print(cores[0], end='')


def texto(msg, cor=0):
    print(cores[cor], end='')
    help(msg)
    print(cores[0], end='')


# programa principal
titulo('Sistema de Visualização PyHelp', cor=4)
while True:
    ajudaComando = input('\033[0;30;43mInsira um comando para visualizar sua documentação: ')
    interactivehelp(ajudaComando)
    continuar = str(input('\033[0;30;41mDeseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('\033[0;30;41mDeseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break