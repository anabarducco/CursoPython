''' Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela com a formatação correta. '''

matriz = list()

for linha in range(0, 3):
    listaLinha = list()
    for coluna in range(0, 3):
        valor = int(input(f'Digite o valor a ser preenchido na posição ({linha},{coluna}): '))
        listaLinha.append(valor)
    matriz.append(listaLinha[:])

print(20*'-')
print(f'{"Matriz Preenchida":^20}')
print(20*'-')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:4}', '|', end='')
    print('\n')