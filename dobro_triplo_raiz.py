#Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a sua raiz quadrada
n1 = int(input('Digite um número: '))
print('{}O dobro de {} é {}. O triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}{}'.format('\033[32m',n1, n1 * 2, n1, n1 * 3, n1, n1 ** (1/2),'\033[m'))