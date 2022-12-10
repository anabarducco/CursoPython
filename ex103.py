''' Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente. '''


def ficha(nomejogador='<desconhecido>', gols=0):
    tamanho = 36 + len(nomejogador)
    print(tamanho*'=')
    print(f'O jogador {nomejogador} marcou {gols} gols na partida.')
    print(tamanho*'=')


#programa principal
nome = input('Insira o nome do jogador: ').title()
qtdGols = input(f'Insira quantos gols o jogador marcou na partida: ')
if qtdGols.isnumeric():
    qtdGols = int(qtdGols)
else:
    qtdGols = 0
if qtdGols != '' and nome != '':
    ficha(nome, qtdGols)
elif nome != '':
    ficha(nome)
elif qtdGols != '':
    ficha(gols=qtdGols)
else:
    ficha()