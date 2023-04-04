#desenvolva uma lógica que leia o peso e a altura de uma pessoa calcule o seu imc e mostre seu status conforme a tabela abaixo
#Abaixo de 18.5 Abaixo do peso
#Entre 18.5 e 25 peso ideal
#30 até 40 obesidade
#acima de 40 obesidade mórbida
from time import sleep
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura * altura)
print('Seu imc é {:.2f}'.format(imc))
print('\033[1;35mANALISANDO DADOS\033[m')
print('+' * 20)
sleep(5)
if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc == 30 or imc < 40:
    print('Você está obeso!')
elif imc > 40:
    print('Você tem obesidade morbida!')