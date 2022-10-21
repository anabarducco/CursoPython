n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
print('A soma dos valores {} e {} é {}'.format(n1,n2,soma))

n3 = float(input('Digite um valor: '))
print(type(n3), n3)

n4 = str(input('Digite um valor: '))
print(type(n4), n4)

n5 = bool(input('Digite um valor: '))
print(type(n5), n5)

n6 = input('Digite algo: ')
print(type(n6), n6, n6.isnumeric())

n7 = input('Digite algo: ')
print(type(n7), n7, n7.isalpha())

n8 = input('Digite algo: ')
print(type(n8), n8, n8.isalnum())