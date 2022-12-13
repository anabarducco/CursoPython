''' Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
Ex: você digita um valor e ele mostra esse valor dobrado, pela metade, aumentado em tantos % e reduzido em tantos %. '''

from desafios_aula22 import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O dobro de {valor} é {moeda.dobro(valor)}.')
print(f'A metade de {valor} é {moeda.metade(valor)}.')
print(f'Com aumento de 10%, {valor} passa a ser {moeda.aumentar(valor)}.')
print(f'Com desconto de 10%, {valor} passa a ser {moeda.diminuir(valor)}.')
