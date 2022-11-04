#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras tem ao to do, sem considerar os espaços
#Quantas letras tem o primeiro nome

nome = input('Insira seu nome completo: ')

nomeSE = nome.replace(' ', '') # substitui os espaços por "não-espaços"
qtdLetras = len(nomeSE) #faz a contagem dos caracteres sem os espaços

nomeSeparado = nome.split() #divide os nomes numa lista de nomes
qtdLetrasPrimeiroNome = len(nomeSeparado[0]) #conta a qtd de caracteres do primeiro nome da lista

print(nome.upper())
print(nome.lower())
print(f'Seu nome tem {qtdLetras} letras.')
print(f'Seu primeiro nome tem {qtdLetrasPrimeiroNome} letras.')