#exercício 108 utilizando packages

from desafios_aula22.utilidadesCeV import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}.')
print(f'Com aumento de 10%, {moeda.moeda(valor)} passa a ser {moeda.moeda(moeda.aumentar(valor))}.')
print(f'Com desconto de 10%, {moeda.moeda(valor)} passa a ser {moeda.moeda(moeda.diminuir(valor))}.')
