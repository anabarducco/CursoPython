''' Crie um programa que leia a idade e o gênero de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
 No final, mostre:
 a) Quantas pessoas têm mais de 18 anos
 b) Quantos homens foram cadastrados
 c) Quantas mulheres têm menos de 20 anos '''

nomes = []
idades = []
generos = []
maiorDezoito = 0
qtdHomem = 0
mulheresMenorVinte = 0

while True:
    print(15*'=-=', '\nCadastro de Nova Pessoa\n', 15*'=-=')
    nome = str(input('Insira o nome: '))
    nomes.append(nome)
    idade = int(input('Insira a idade: '))
    idades.append(idade)
    if idade > 18:
        maiorDezoito += 1
    while True:
        genero = str(input('Insira o gênero (formato [F/M]): ')).upper()
        generos.append(genero)
        if genero == 'F' or genero == 'M':
            if genero == 'M':
                qtdHomem += 1
            elif genero == 'F':
                if idade < 20:
                    mulheresMenorVinte += 1
            break
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break

print(15*'=-=')
print(f'Das pessoas cadastradas, temos:\n{maiorDezoito} pessoas com mais de 18 anos;\n{qtdHomem} homens;\n{mulheresMenorVinte} mulheres com menos de vinte anos.')