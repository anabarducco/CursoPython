#Operações em Python
"""
+ : soma
- : subtração
* : multiplicação
/ : divisão
** : potência
// : divisão inteira
% : resto da divisão
= : atribuição
== : operador de comparação
"""

#Ordem de Precedência
"""
()
**
* / // %
+ -
"""

nome = input('Insira seu nome: ')
print(f'Seja bem-vindo, {nome}!')
print(f'Seja bem-vindo, {nome:20}!')
print(f'Seja bem-vindo, {nome:>20}!')
print(f'Seja bem-vindo, {nome:<20}!')
print(f'Seja bem-vindo, {nome:^20}!')
print(f'Seja bem-vindo, {nome:=^20}!')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print(f'A soma vale {n1+n2}')
print(f'A subtração vale {n1-n2}')
print(f'A multiplicação vale {n1*n2}')
print(f'A divisão vale {n1/n2:.3f}')
print(f'A potência vale {n1**n2}')
print(f'A divisão inteira vale {n1//n2}')
print(f'O resto da divisão vale {n1%n2}')