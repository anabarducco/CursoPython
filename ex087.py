''' Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados
b) A soma de todos os valores da terceira coluna
c) O maior valor da segunda linha '''

matriz = list()

par = list()
somaPar = 0

terceiraColuna = list()
somaTerceiraColuna = 0

maiorValorSegundaLinha = None

for linha in range(0, 3):
    listaLinha = list()
    for coluna in range(0, 3):
        valor = int(input(f'Digite o valor a ser preenchido na posição ({linha},{coluna}): '))
        listaLinha.append(valor)
        if valor % 2 == 0:
            par.append(valor)
            somaPar += valor
        if coluna == 2:
            terceiraColuna.append(valor)
            somaTerceiraColuna += valor
        if linha == 1:
            if maiorValorSegundaLinha == None or valor > maiorValorSegundaLinha:
                maiorValorSegundaLinha = valor
    matriz.append(listaLinha[:])

print(20*'-')
print(f'{"Matriz Preenchida":^20}')
print(20*'-')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:4}', '|', end='')
    print('\n')
print(20*'-')
print(f'Os valores pares digitados foram: {par}.')
print(f'A soma desses valores resulta em {somaPar}.')
print(20*'-')
print(f'Os valores digitados na terceira coluna foram: {terceiraColuna}.')
print(f'A soma desses valores resulta em {somaTerceiraColuna}.')
print(20*'-')
print(f'Os valores digitados na segunda linha foram: {matriz[1]}.')
print(f'Dentre eles, o maior valor digitado foi {maiorValorSegundaLinha}.')
print(20*'-')