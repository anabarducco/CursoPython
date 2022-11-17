''' Laços de repetição - parte 1: FOR i IN RANGE (x, y) '''

for c in range(0, 6):
    print('Oi')
print('Fim')

print(10*'=')

for c in range(0, 6):
    print('Oi')
    print('Fim')

print(10 * '=')

for c in range(0, 6):
    print(c)
print('Fim')

print(10 * '=')

for c in range(6, 0, -1):
    print(c)
print('Fim')

print(10 * '=')

for c in range(0, 10, 2):
    print(c)
print('Fim')

print(10 * '=')

i = int(input('Insira um número inteiro: '))
for c in range(0, i+1):
    print(c)
print('Fim')

print(10 * '=')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

print(10 * '=')

soma = 0
for c in range(0, 4):
    i = int(input('Insira um valor: '))
    soma += i
print(f'Soma = {soma}')