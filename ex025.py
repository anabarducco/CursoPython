#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = input('Insira seu nome completo: ')
temSilva = 'Silva' in nome

print(f'Tem "Silva" no nome: {temSilva}')