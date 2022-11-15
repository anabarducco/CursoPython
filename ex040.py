''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
 acordo com a média atingida:
 Média abaixo de 5.0: reprovado;
 Média entre 5.0 e 6.9: recuperação;
 Média 7.0 ou superior: aprovado. '''

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2)/2

if media < 5.0:
    print(f'O aluno foi reprovado com média final {media}.')
elif media > 5.0 and media < 6.9:
    print(f'O aluno está de recuperação com média final {media}.')
elif media>= 7.0:
    print(f'O aluno foi aprovado com média final {media}.')