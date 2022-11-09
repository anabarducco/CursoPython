'''Cores no Terminal
\033[style; text; backgroundm
    ex: \033[0; 33; 44m

Style:
    0: none
    1: bold
    4: underline
    7: negative

Text (30)/Background (40):
    30/40: branco
    31/41: vermelho
    32/42: verde
    33/43: amarelo
    34/44: azul
    35/45: roxo
    36/46: verde água
    37/47: cinza
'''

print('\033[0;30;41mTeste\033[m')
print('\033[4;33;44mTeste\033[m')
print('\033[1;35;43mTeste\033[m')
print('\033[30;42mTeste\033[m')
print('\033[mTeste\033[m')
print('\033[7;30mTeste\033[m')

print('\033[1;31mTeste\033[m')
print('\033[0;31mTeste\033[m')

a=3
b=2
c = a+b

print(f'A soma de \033[32m{a}\033[m e \033[35m{b}\033[m é \033[34m{c}\033[m')

nome = 'Ana Beatriz'
print(f'Olá, muito prazer em te conhecer, \033[4;35m{nome}\033[m!!!')

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'peb':'\033[7;30m'}
print(f'Olá, muito prazer em te conhecer, {cores["vermelho"]}{nome}{cores["limpa"]}!!!')