''' Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de textos
simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas. '''

from ex_115 import sistema
from ex_115 import operacoes

while True:
    sistema.menu()
    op = operacoes.leiaint()
    operacoes.opvalido(op)