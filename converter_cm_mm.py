#faça um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
n1 = float(input('Digite um valor um metros: '))
print('\033[1mO valor de {} convertido para centímetros é {}'.format(n1, n1*100))
print('\033[1mO valor de {} em milímetros é {}'.format(n1, n1*1000))