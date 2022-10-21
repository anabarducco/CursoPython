#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Insira o valor em metros: '))
print(f'Esse valor em centímetros equivale a {valor*100}cm e em milímetros equivale a {valor*1000}mm.')

#Desafio: ler o valor em metros e exibir sua conversão de Km a Mm.
metros = float(input('Insira o valor em metros: '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000
print(f'Esse valor equivale a {km}km, {hm}hm, {dam}dam, {dm}dm, {cm}cm e {mm}mm.')