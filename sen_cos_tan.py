#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste angulo
import math
from time import sleep
print('\033[1;34m-+-\033[m'*25)
angulo = float(input('Informe o valor do ângulo: '))
print('Estamos calculando...')
sleep(3)
print('\033[1;35m-+-\033[m'*25)
print('O valor do seno deste ângulo é: ', (math.sin(math.radians(angulo))))
print('O valor do cosseno deste ângulo é ', (math.cos(math.radians(angulo))))
print('O valor da tangente deste ângulo é ', (math.tan(math.radians(angulo))))

