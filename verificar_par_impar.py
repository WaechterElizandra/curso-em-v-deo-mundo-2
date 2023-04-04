#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
from time import sleep
num = int(input('Digite um número: '))
print('\033[1;36m-=-\033[m'*25)
print('Um momento, estou analisando o seu valor!')
print('\033[1;36m-=-\033[m'*25)
sleep(5)
if num % 2 == 0:
    print('Este número é par!')
else:
    print('Este número é ímpar!!')