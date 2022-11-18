''' Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
 da progressão utilizando a estrutura while. '''

primeiroTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimoTermo = primeiroTermo + (10-1) * razao

print(primeiroTermo, end=' → ')
while primeiroTermo != decimoTermo:
    primeiroTermo += razao
    print(primeiroTermo, end=' → ')
print('FIM')