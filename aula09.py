'''Exemplo do vídeo: fatiamento de string'''

frase = 'Curso em Vídeo Python'
print(frase[9]) #printa somente o caractere da pos 9
print(frase[9:21]) #printa os caracteres da pos 9 a pos 20
print(frase[9:21:2]) #printa de 2 em 2 caracteres da pos 9 a pos 20
print(frase[:5]) #printa do início (0) a pos 4
print(frase[15:]) #printa a partir da pos 15 até o final
print(frase[9::3]) #printa de 3 em 3 caracteres da pos 9 até o final

#Análise de String
print(len(frase)) #quantidade de caracteres da string (0-20 => 21)
print(frase.count('o')) #quantidade de vezes que aparece o caractere 'o' na string
print(frase.count('o', 0, 13)) #quantidade de vezes que aparece o caractere 'o' do início até a pos 12
print(frase.find('deo')) #posição que aparece/inicia a sequencia 'deo'
print(frase.find('android')) #como não existe, retorna -1, pq não foi encontrado
print('Curso' in frase) #retorna se existe ou não

#Transformação de String
print(frase.replace('Python', 'Android')) #substituí a primeira palavra pela segunda
print(frase.upper()) #coloca tudo em maiúsculas
print(frase.lower()) #coloca tudo em minúsculas
print(frase.capitalize()) #apenas o primeiro caractere em maiúsculo
print(frase.title()) #o primeiro caractere de cada palavra em maiúsculo

frase2 = '   Aprenda Python  '
print(frase2.strip()) #remove espaços desnecessários no início e no final
print(frase2.rstrip()) #remove somente os espaços desnecessários do lado direito da string
print(frase2.lstrip()) #remove somente os espaços desnecessários do lado esquerdo da string

#Divisão de String
frase3 = frase.split() #divide a string de x palavras em uma lista de x strings, onde tiver espaços
print(frase3)

#Junção de Strings
print('-'.join(frase3)) #junta as strings da lista de strings com o separador '-'