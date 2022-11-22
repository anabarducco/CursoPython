''' Variáveis Compostas - LISTAS
Listas ficam entre [] e podem ser MUTÁVEIS
Para adcionar um elemento no final da lista, é utilizado o método APPEND()
Para adicionar um elemento numa posição específica, é utilizado o método INSERT(posição, elemento)
Para eliminar um elemento, pode-se utilizar o comando DEL lista[posição], o método POP(posição)
ou o método REMOVE(elemento)
O método POP() sem indicar a posição elimina o último elemento
É possível gerar uma lista com o método LIST() passando o RANGE() como parâmetro
O método SORT() ordena os valores em ordem crescente, e passando REVERSE = True como parâmetro de SORT(), os valores
são ordenados em ordem decrescente
E o método LEN() indica o tamanho da LISTA
'''

numTupla = (2, 5, 9, 1)
print(numTupla)

numLista = [2, 5, 9, 1]
print(numLista)
numLista[2] = 3
print(numLista)
numLista.append(7)
print(numLista)
numLista.sort()
print(numLista)
numLista.sort(reverse=True)
print(numLista)
tamanhoLista = len(numLista)
print(tamanhoLista)
numLista.insert(2, 2)
print(numLista)
numLista.pop()
print(numLista)
numLista.pop(2)
print(numLista)
if 4 in numLista:
    numLista.remove(4)
    print(numLista)
else:
    print('Não encontrei o número 4.')

novaLista = list()
novaLista.append(5)
novaLista.append(9)
novaLista.append(4)
for valor in novaLista:
    print(valor)
for posiçao, valor in enumerate(novaLista):
    print(f'O valor {valor} se encontra na posição {posiçao}.')
print('Final da Lista.')

for contagem in range(0, 5):
    novaLista.append(int(input('Digite um número inteiro: ')))
for posiçao, valor in enumerate(novaLista):
    print(f'O valor {valor} se encontra na posição {posiçao}.')
print('Final da Lista.')

a = [2, 3, 4, 5]
b = a
c = a[:] #"fatiar" a lista, como com Strings, produz a cópia da lista, e elas não se igualam. Então ao alterar uma, a outra se mantém.
b[2] = 8 #em Python, ao atribuir uma lista à outra, elas se igualam. Então ao alterar uma, altera-se a outra também.
c[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')