''' Laços de Repetição '''

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
print('Acabou')

#

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')