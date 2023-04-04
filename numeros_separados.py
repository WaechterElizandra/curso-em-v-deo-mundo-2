#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from time import sleep
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
sleep(3)
print('Calma...EStou fazendo os cálculos para você!'.upper())
sleep(5)
print('\033[1mO número informado é {}'.format(num))
print('\033[1mA unidade vale {}'.format(u))
print('\033[1mA dezena vale {}'.format(d))
print('\033[1mA centena vale {}'.format(c))
print('O milhar vale {}'.format(m))