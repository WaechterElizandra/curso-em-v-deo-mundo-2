#Crie um programa que leia a altura e a largura de uma parede calcule sua area em metros e a quantidade de tinta necessária para pintá-la, sabendo que cda litro de tinta pinta 2m²
altura = float(input('Informe a altura da parede: '))
largura = float(input('Infrome a largura da parede: '))
area = altura * largura
tinta = area /2
print('A área a ser pintada é de {}{}m²{}, e você irá precisar de {}{}L{} de tinta'.format('\033[1;32m',area,'\033[m','\033[1;31m',tinta,'\033[m'))