''' Variáveis compostas: TUPLAS
variáveis simples (recebem um único valor) x compostas (podem receber 2 ou mais valores)
 os elementos das variáveis compostas são identificados por índices, iniciando no 0
 uma string é uma variável composta do tipo LISTA, em que os caracteres são armazenados em diferentes índices
 variáveis compostas podem ser fatiadas, assim como visto nas strings
 elas também podem ser utilizadas em estruturas de repetição como o range (FOR i in VARIAVEL_COMPOSTA)

 as TUPLAS são IMUTÁVEIS: não é possível mudar o elemento da tupla após defini-lo
 também não é possível deletar um elemento da tupla, apenas ela inteira

 variáveis compostas podem ser de 3 tipos diferentes: tuplas (), listas [] ou dicionário {} '''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')

print(len(lanche))
for contador in range(0, len(lanche)):
    print(f'O item {contador+1} de lanche é {lanche[contador]}.')
print('Todos os itens de lanche foram apresentados.')

for pos, comida in enumerate(lanche):
    print(f'A posição {pos} de lanche é {comida}.')
print('Todos os itens de lanche foram apresentados.')

print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(f'O número 5 aparece {c.count(5)} vezes na tupla c.')
print(f'O número 2 aparece {d.count(2)} vezes na tupla d.')
print(f'O número 8 está na posição {c.index(8)} na tupla {c}.')
print(f'O número 8 está na posição {d.index(8)} na tupla {d}.')

pessoa = ('Ana Beatriz', 20, 'F', 1.67, 65)
print(pessoa)