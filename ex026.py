#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
fraseCortada = frase.strip()
fraseMaiuscula = fraseCortada.upper()

qtdA = fraseMaiuscula.count('A')
posInicialA = fraseMaiuscula.find('A')
posFinalA = fraseMaiuscula.rfind('A')

print(f'A letra "A" aparece {qtdA} vezes.')
print(f'A primeira vez que a letra "A" aparece é na posição {posInicialA}.')
print(f'A última vez que a letra "A" aparece é na posição {posFinalA}.')