#Utilização de módulos (bibliotecas python)
#import xxx: importa toda a biblioteca// from xxx import yyy: importa função específica da biblioteca
#PyPI - Python Package Index: precisa instalar a biblioteca (install package xxx) para utilizá-la. É possível criar uma biblioteca
#e disponibilizá-la para outras pessoas através desses pacotes.
#É possível ver/adicionar/excluir esses packages em "Preferences" > "Project Interpreter"

import math #importa toda a biblioteca math
#from math import sqrt #só importa a função sqrt da biblioteca math
import random

num = int(input('Digite um número inteiro: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é {raiz:.3f}.')
print(f'Arredondando para cima, a raiz de {num} é {math.ceil(raiz)}.')
print(f'Arredondando para baixo, a raiz de {num} é {math.floor(raiz)}.')

numRandom = random.random() #gera float aleatório entre 0 e 1
intRandom = random.randint(0,100) #gera int aleatório entre os limitadores
print(f'Float aleatório gerado: {numRandom}.\nInt aletório gerado: {intRandom}.')