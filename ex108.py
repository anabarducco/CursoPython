''' Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
como um valor monetário formatado. '''

from desafios_aula22 import moeda

valor = float(input('Digite o valor do produto: R$'))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}.')
print(f'Com aumento de 10%, {moeda.moeda(valor)} passa a ser {moeda.moeda(moeda.aumentar(valor))}.')
print(f'Com desconto de 10%, {moeda.moeda(valor)} passa a ser {moeda.moeda(moeda.diminuir(valor))}.')
