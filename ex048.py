''' Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de 3 e que se encontram
 no intervalo de 1 até 500. '''

soma = 0
for i in range(1, 500):
    if i % 2 == 1:
        if i % 3 == 0:
            soma += i
            #print(i, soma)
print(f'A soma dos número ímpares múltiplos de 3 entre 1 e 500 é igual a {soma}.')