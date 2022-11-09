''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250.00, calcule um aumento de 10%.
Para inferiores ou iguais, calcule um aumento de 15%.'''

salario = float(input('Digite o seu salário atual: '))

if salario > 1250:
    salario += salario*0.1
else:
    salario += salario * 0.15

print(f'Com o aumento, seu salário será R${salario:.2f}')