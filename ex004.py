#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

entrada = input('Digite algo: ')
print(f'Informações sobre "{entrada}":')
print(f'Tipo de dado: {type(entrada)}')
print(f'É alfabético: {entrada.isalpha()}')
print(f'É numérico: {entrada.isnumeric()}')
print(f'É alfanumérico: {entrada.isalnum()}')
print(f'É caractere ASCII: {entrada.isascii()}')
print(f'É dígito: {entrada.isdigit()}')
print(f'É decimal: {entrada.isdecimal()}')
print(f'É identificador: {entrada.isidentifier()}')