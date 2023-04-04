#faça um programa que converta uma temperatura informada em ºc para ºf
celsius = float(input('Informe a temperatura em ºC:'))
fahrenheit = (celsius * 9/5) + 32
print('\033[7mA temperatura de {}ºC convertida é igual a {}ºF'.format(celsius, fahrenheit))