#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo calcule e mostre o comprimento da hipotenusa.
from math import hypot
from time import sleep
catetoo = float(input('Informe o valor do cateto oposto: '))
catetoa = float(input('Digite o valor do cateto adjacente: '))
print('\033[35mANALISANDO VALORES!\033[m')
sleep(5)
print('O valor da \033[1mHipotenusa\033[m é ',int(hypot(catetoo,catetoa)))
