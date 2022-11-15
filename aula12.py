''' Condições aninhadas: else-elif-if
Começa com if -> pode ter um ou mais "else-if" ELIF -> termina com else '''

nome = str(input('Qual é o seu nome? '))
if nome == 'Ana Beatriz':
    print('Que nome bonito!')
elif nome == 'João Vitor':
    print('Que nome legal!')
elif nome in 'Maria José':
    print('Seu nome é bíblico!')
else:
    print('Que nome normal!')
print(f'Tenha um bom dia, {nome}!')