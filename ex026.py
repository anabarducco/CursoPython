#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')

qtdA = frase.count('A')
qtda = frase.count('a')
qtdATotal = qtdA + qtda

posA = frase.find('A')
posa = frase.find('a')
if posA < posa and posA != -1:
    posInicialA = posA
else:
    if posa != -1:
        posInicialA = posa
    else:
        posInicialA = -1

posA = frase.rfind('A')
posa = frase.rfind('a')
if posA > posa:
    posFinalA = posA
else:
    posFinalA = posa

print(f'A letra "A" aparece {qtdATotal} vezes.')
print(f'A primeira vez que a letra "A/a" aparece é na posição {posInicialA}.')
print(f'A última vez que a letra "A/a" aparece é na posição {posFinalA}.')