# utilizando pacote uteispct
from uteispct import numeros

num = int(input('Digite um valor: '))

fat = numeros.fatorial(num)
dob = numeros.dobro(num)
trip = numeros.triplo(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dob}.')
print(f'O tiplo de {num} é {trip}.')