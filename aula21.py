''' Funções - pt. 2
Interactive Help/ Ajuda interativa:
função interna help() no console - ao digitar qualquer comando python, é mostrada a documentação/manual do comando
para sair, basta escrever quit
help(comando) printa no console a documentação do comando também
print(comando.__doc__) também printa a documentação do comando

Docstrings - string de documentação
Começa exatamente depois do comando def nomefunção()
Basta abrir """ """ e escrever entre as aspas a documentação

Parâmetros Opcionais
Atribuir valores de parâmetros na função, para caso uma das variáveis não receba valor na chamada da função
Ex:
def soma(a, b, c):
    s = a + b + c
    print(s)
soma(1, 3, 4) ==> funciona normal
soma(1, 3) ==> dá erro
def soma(a, b, c=0):
    s = a + b + c
    print(s)
soma(1, 3, 4) ==> funciona normal
soma(1, 3) ==> funciona também

Escopo de Variáveis
Variáveis no programa principal funcionam no programa tdo ==> escopo global
Variáveis em funções só funcionam nessas funções ==> escopo local

Retornando Vaores
Ao invés de printar o resultado da função, é possível retornar o valor com RETURN
Ex:
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = soma(1, 2, 3) ==> retorna 6
r2 = soma(1, 2) ==> retorna 3
r3 = soma(1) ==> retorna 1
print(r1, r2, r3)
'''


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n1 = int(input('Digite um número: '))
print(f'O fatorial de {n1} é {fatorial(n1)}.')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f1, f2, f3)


def parouimpar(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


n2 = int(input('Digite um número: '))
if parouimpar(n2):
    print('É par!')
else:
    print('É ímpar!')