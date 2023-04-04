#desenvolva um programa que pergunte a distância de uma viagem em km. calcule o preço da passagem
# cobrando 0.50 por viagem até 200km e 0.45 para viagens mais longas
distancia = float(input('Digite a distância da sua viagem: '))
print('Você fará um viagem de {} km'.format(distancia))
if distancia <= 200:
    print('\033[4mO valor da sua viagem custará R$ {:.2f}\033[m'.format(distancia * 0.5))
else:
    print('\033[4mO valor da sua viagem custará R$ {:.2f}\033[m'.format(distancia * 0.45))