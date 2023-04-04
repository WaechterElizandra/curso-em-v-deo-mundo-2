#DEsenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar  um triângulo
from time import sleep
reta1 = float(input('Informe o valor da 1ª reta: '))
reta2 = float(input('Informe o valor da 2ª reta: '))
reta3 = float(input('Informe o valor da 3ª reta: '))
print('+-'*20)
print('\033[1;31mANALISANDO OS DADOS...\033[m')
print('+-'*20)
sleep(5)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
