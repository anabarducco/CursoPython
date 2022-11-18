''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
 Caso esteja errado, peça a digitação novamente até ter um valor correto. '''

genero = str(input('Digite seu gênero no formato [M/F]: ')).strip().upper()
while genero not in 'MF':
    genero = str(input('Formato errado. Por favor, digite seu gênero no formato [M/F]: ')).strip().upper()

print(f'Gênero {genero} registrado com sucesso!')