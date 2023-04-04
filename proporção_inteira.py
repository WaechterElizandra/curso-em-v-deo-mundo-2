#crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira ex: 6.127 mostra a parte inteira 6
from math import trunc
num = float(input('\033[35mDigite um número inteiro:Ex: 5.894 \033[m'))
print('A parte inteira deste número é: ',trunc(num))
