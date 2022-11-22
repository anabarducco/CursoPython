''' Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares. '''

valores = ()
numerosPares = ()

for i in range(0, 4):
    valor = int(input('Insira um valor: '))
    valores += (valor, )
    if valor % 2 == 0:
        numerosPares += (valor, )

print(f'O número 9 aparece {valores.count(9)} vezes.')
print(f'O número 3 aparece primeiro na posição {valores.index(3)+1}.')
print(f'Os números pares digitados foram {numerosPares}.')