''' Crie um código em Python que teste se o site pudim.com.br está acessivel pelo computador usado. '''

import requests

try:
    requests.get(url='http://pudim.com.br').status_code == 200
except:
    print('Infelizmente não consegui acessar o site do pudim.')
else:
    print('Consegui acessar o site do pudim!')
