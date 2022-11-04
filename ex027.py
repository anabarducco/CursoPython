#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Exemplo: Ana Maria de Souza => Primeiro: Ana; Último: Souza.

nomeCompleto = input('Digite seu nome completo: ')
nomeDividido = nomeCompleto.split()
qtdNomes = len(nomeDividido)

print(f'Primeiro nome = {nomeDividido[0]}\nÚltimo nome = {nomeDividido[qtdNomes-1]}')