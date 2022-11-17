''' Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
 só que faça agora utilizando um laço FOR. '''

num = int(input('Insira um número inteiro: '))
print(f'A tabuada de {num} é:')
for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')
    i+=1