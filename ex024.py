#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

nomeCidade = input('Digite o nome de uma cidade: ')
nomeCidadeDividida = nomeCidade.split()
comecaSanto = 'Santo' in nomeCidadeDividida[0]

print(f'Essa cidade começa com "Santo": {comecaSanto}')