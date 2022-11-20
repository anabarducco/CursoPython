''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo. '''
import time

print(15*'=-=', '\nTabuada\n', 15*'=-=')
while True:
    num = int(input('Qual tabuada você deseja ver? '))
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{i} x {num} = {i * num}')
    print(15*'=-=')
print('Finalizando o programa.')
time.sleep(2.0)