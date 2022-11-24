''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. '''

parentesesAberto = list()
parentesesFechado = list()

expressao = str(input('Digite uma expressão matemática: '))

for contador in range(0, len(expressao)):
    if expressao[contador] == '(':
        parentesesAberto.append(contador)
    if expressao[contador] == ')':
        parentesesFechado.append(contador)

print(parentesesAberto)
print(parentesesFechado)

if len(parentesesAberto) != len(parentesesFechado):
    print('A expressão foi escrita incorretamente.')
else:
    for contador in range(0, len(parentesesAberto)):
        if parentesesAberto[contador] > parentesesFechado[contador]:
            print('A expressão foi escrita incorretamente.')
            break
        else:
            print('A expressão foi escrita corretamente.')
            break