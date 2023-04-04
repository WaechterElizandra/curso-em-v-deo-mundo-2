#refaça o Desafio009 mostrando a tabuada de um número que o usuário digitar só que usando um laço for
#DESAFIO 009 faça um programa que leia um número inteiro e mostre na tela a sua tabuada
n = int(input('Digite o número da tabuada que deseja: '))
print('\033[1;32m*\033[m'*15)
for c in range(0,11):
    print(n, 'X', c, '=', n * c)
print('\033[1;32m*\033[m'*15)