#escreva um programa que leia a velocidade de um carro. se ele ultrapassar 80km/h mostre uma mensagemdizendo que foi multado. A multa vai custar
#7.00 reais cada km acima do limite
velocidade = float(input('Informe a velocidade do carro em km/h: '))
if velocidade > 80.0:
    print('\033[1;31mVocê excedeu limite de velocidade de 80km/h\033[m')
    print('Você foi multado em R$ {:.2f}'.format((velocidade - 80) * 7))
else:
    print('\033[1;32mVocê está dentro do limite de velocidade! Parabéns!!\033[m ')