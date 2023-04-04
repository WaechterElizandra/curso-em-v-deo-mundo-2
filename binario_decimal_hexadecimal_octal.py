#faça um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será  a base da conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

n1 = int(input('Informe um número: '))
conversao = input('Digite o número da conversão que deseja fazer: 1-BINÁRIO 2-OCTAL 3-HEXADECIMAL ')
if conversao == '1':
   print('O número {} convertido para o sistema BINÁRIO é igual a {}'.format(n1,bin(n1)[2:])) #bin() é uma funçao que transforma um n decimal em binário
elif conversao == '2':
    print('O número {} convertido para OCTAL é igual a {}'.format(n1,oct(n1)[2:]))#oct() é uma funçao para transformar um n decimal em octal
elif conversao == '3':
    print('O número {} convertido para hexadecimal é igual a {}'.format(n1,hex(n1)[2:]))
else:
    print('O valor informado não corresponde com as conversões disponíveis. Tente novamente!')