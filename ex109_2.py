#exercício 109 utilizando packages

from desafios_aula22.utilidadesCeV import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}.')
print(f'Com aumento de 10%, {moeda.moeda(valor)} passa a ser {moeda.aumentar(valor, True)}.')
print(f'Com desconto de 10%, {moeda.moeda(valor)} passa a ser {moeda.diminuir(valor, True)}.')