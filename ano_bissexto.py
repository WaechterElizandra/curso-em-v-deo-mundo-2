#faça um programa que leia um ano qualquer e mostre se ele é bissexto
from calendar import isleap
ano = int(input('Digite um ano: '))
if isleap(ano):
    print('Este ano é bissesto')
else:
    print('Este ano não é bissexto!')
