''' Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função
chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para
aceitar apenas valores que sejam monetários. '''

from desafios_aula22.utilidadesCeV import moeda
from desafios_aula22.utilidadesCeV import dados

valor = dados.leiadinheiro()
moeda.resumo(valor)