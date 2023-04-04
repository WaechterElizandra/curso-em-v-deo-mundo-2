#faça um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelo qual ele foi alugado. Calcule o preço a pagar
#sabendo que o carro custa 60.00 por dia e 0.15 o km rodado
dias = int(input('Quandos dias o carro foi alugado? '))
kmrodados = float(input('Quantos KMs foram rodados? '))
print('_' * 20)
print('\033[1;37mTotal de dias alugado: {}'.format(dias))
print('\033[1;37mTotal de KM rodados: {}'.format(kmrodados))
print('\033[1;37mTotal a pagar:{:.2f}'.format((dias * 60.00)+ kmrodados * 0.15))
print('_' * 20)