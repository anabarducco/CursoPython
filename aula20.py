'''Funções - pt. 1
def nomeFunção():
    o que a função vai fazer
pra seguir para o programa "normal", é necessário pular 2 linhas

def nomeFunção(parâmetro):
    o que a função vai fazer
    print(parametro)

no programa normal:
nomeFunção(parâmetroPassado) ==> a função vai printar "parâmetroPassado"

empacotamento de parâmetros: quando você passa diferentes quantidades de parâmetros pra função
def função(*num) ==> não sei quantos parâmetros serão passados, mas a quantidade que for, é passada pra "num"
'''


def titulo(texto):
    print(30*'-')
    print(texto)
    print(30*'-')


def soma(a, b):
    print(f'A = {a}')
    print(f'B = {b}')
    s = a + b
    print(f'{a} + {b} = {s}')


def contador(*num):
    tamanho_contador = len(num)
    print(f'Foram digitados {tamanho_contador} números.')
    for valor in num:
        print(valor, end=' ')
    print('FIM')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def soma_valores(*num):
    soma = 0
    for valor in num:
        soma += valor
    print(soma)


titulo('Curso em Vídeo')
titulo('Aprenda Python')
titulo('Ana Beatriz Barducco')

soma(8, 9)
soma(4, 5)
soma(2, 1)
soma(a=4, b=5)
soma(b=4, a=5)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)

soma_valores(1, 2)
soma_valores(1, 2, 3)
soma_valores(1, 2, 3, 4)