#exercício 107 utilizando packages

from desafios_aula22.utilidadesCeV import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O dobro de {valor} é {moeda.dobro(valor)}.')
print(f'A metade de {valor} é {moeda.metade(valor)}.')
print(f'Com aumento de 10%, {valor} passa a ser {moeda.aumentar(valor)}.')
print(f'Com desconto de 10%, {valor} passa a ser {moeda.diminuir(valor)}.')