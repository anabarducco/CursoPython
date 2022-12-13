# utilizando arquivo uteis.py
import uteis

num = int(input('Digite um valor: '))

fat = uteis.fatorial(num)
dob = uteis.dobro(num)
trip = uteis.triplo(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {dob}.')
print(f'O tiplo de {num} é {trip}.')